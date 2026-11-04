using System.Text.Json;

namespace VietCv;

/// <summary>Lưu hồ sơ + file sinh ra trong DATA_DIR (mặc định ./data, mount volume khi chạy Docker).</summary>
public sealed class Store
{
    private static readonly JsonSerializerOptions Json = new()
    {
        PropertyNamingPolicy = JsonNamingPolicy.CamelCase,
        PropertyNameCaseInsensitive = true,
        WriteIndented = true,
        Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping,
    };

    public string Root { get; }
    public string ProfilesDir => Path.Combine(Root, "profiles");
    public string OutDir => Path.Combine(Root, "out");
    public Taxonomy Taxonomy { get; }

    public Store(string root)
    {
        Root = root;
        Directory.CreateDirectory(ProfilesDir);
        Directory.CreateDirectory(OutDir);
        var taxPath = Path.Combine(AppContext.BaseDirectory, "content", "bank.json");
        var bank = JsonSerializer.Deserialize<JsonElement>(File.ReadAllText(taxPath));
        Taxonomy = new Taxonomy
        {
            Aliases = bank.GetProperty("aliases").Deserialize<Dictionary<string, List<string>>>(Json) ?? new(),
            Watchlist = bank.GetProperty("watchlist").Deserialize<List<string>>(Json) ?? new(),
        };
        Seed();
    }

    private void Seed()
    {
        var seed = Path.Combine(AppContext.BaseDirectory, "Cv", "seed-profile.json");
        if (File.Exists(seed) && ListIds().Count == 0)
            File.Copy(seed, Path.Combine(ProfilesDir, "vuhuudo.json"));
    }

    public List<string> ListIds() =>
        Directory.Exists(ProfilesDir)
            ? Directory.GetFiles(ProfilesDir, "*.json").Select(f => Path.GetFileNameWithoutExtension(f)).OrderBy(x => x).ToList()
            : new();

    private static string SafeId(string id)
    {
        if (!System.Text.RegularExpressions.Regex.IsMatch(id, "^[A-Za-z0-9_-]{1,40}$"))
            throw new InvalidOperationException("id hồ sơ chỉ gồm chữ, số, - và _");
        return id;
    }

    public Profile? Load(string id)
    {
        var path = Path.Combine(ProfilesDir, SafeId(id) + ".json");
        return File.Exists(path) ? JsonSerializer.Deserialize<Profile>(File.ReadAllText(path), Json) : null;
    }

    public void Save(string id, Profile p)
    {
        var path = Path.Combine(ProfilesDir, SafeId(id) + ".json");
        File.WriteAllText(path, JsonSerializer.Serialize(p, Json));
    }

    public string DirFor(string id, string role)
    {
        var d = Path.Combine(OutDir, SafeId(id), CvLogic.Slug(role));
        Directory.CreateDirectory(d);
        return d;
    }

    public static string Dump(Profile p) => JsonSerializer.Serialize(p, Json);
}
