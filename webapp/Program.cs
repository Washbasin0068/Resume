using System.Text.Json;
using VietCv;

var builder = WebApplication.CreateBuilder(args);
builder.Services.Configure<Microsoft.AspNetCore.Http.Features.FormOptions>(o =>
{
    o.MultipartBodyLengthLimit = 20 * 1024 * 1024;
});
var app = builder.Build();

var dataDir = Environment.GetEnvironmentVariable("DATA_DIR")
              ?? Path.Combine(AppContext.BaseDirectory, "..", "..", "..", "..", "data");
var store = new Store(Path.GetFullPath(dataDir));
var json = new JsonSerializerOptions(JsonSerializerDefaults.Web) { Encoder = System.Text.Encodings.Web.JavaScriptEncoder.UnsafeRelaxedJsonEscaping };

app.UseDefaultFiles();
app.UseStaticFiles();

app.MapGet("/api/health", () => Results.Ok(new { ok = true, chrome = Pdf.Chrome(), data = store.Root }));

app.MapGet("/api/profiles", () => Results.Ok(store.ListIds()));

app.MapGet("/api/profiles/{id}", (string id) =>
{
    var p = store.Load(id);
    return p is null ? Results.NotFound(new { error = $"Không thấy hồ sơ {id}" }) : Results.Json(p, json);
});

app.MapPut("/api/profiles/{id}", (string id, Profile p) =>
{
    store.Save(id, p);
    return Results.Ok(new { saved = id });
});

app.MapPost("/api/render", (RenderRequest req) =>
{
    try
    {
        // Ưu tiên id người dùng đang chọn; nếu không có thì suy từ tên.
        var id = !string.IsNullOrWhiteSpace(req.ProfileId) ? req.ProfileId!
            : !string.IsNullOrWhiteSpace(req.Profile?.Name.GetValueOrDefault("en")) ? CvLogic.Slug(req.Profile!.Name["en"])
            : "default";
        var profile = req.Profile ?? store.Load(id) ?? throw new InvalidOperationException("Thiếu hồ sơ");
        if (string.IsNullOrWhiteSpace(req.Role)) throw new InvalidOperationException("Chưa nhập role");
        var langs = req.Langs is { Count: > 0 } ? req.Langs : new List<string> { "EN", "VI" };
        if (req.Profile is not null) store.Save(id, req.Profile);
        var res = Generator.Render(store, id, profile, req.Role, req.Title, langs);
        return Results.Json(res, json);
    }
    catch (Exception ex)
    {
        return Results.BadRequest(new { error = ex.Message });
    }
});

app.MapPost("/api/improve", async (HttpRequest request) =>
{
    try
    {
        if (!request.HasFormContentType) return Results.BadRequest(new { error = "Gửi file dạng multipart" });
        var form = await request.ReadFormAsync();
        var file = form.Files.FirstOrDefault() ?? throw new InvalidOperationException("Chưa chọn file");
        using var ms = new MemoryStream();
        await file.CopyToAsync(ms);
        var profile = store.Load(form["profileId"].FirstOrDefault() ?? "") ?? new Profile();
        var result = CvLogic.Improve(file.FileName, ms.ToArray(), profile, store.Taxonomy);
        return Results.Json(result, json);
    }
    catch (Exception ex)
    {
        return Results.BadRequest(new { error = ex.Message });
    }
});

app.MapGet("/files/{id}/{role}/{name}", (string id, string role, string name) =>
{
    var root = Path.GetFullPath(store.OutDir) + Path.DirectorySeparatorChar;
    var path = Path.GetFullPath(Path.Combine(root, id, role, name));
    if (!path.StartsWith(root, StringComparison.Ordinal) || !File.Exists(path)) return Results.NotFound();
    return Results.File(path, name.EndsWith(".pdf") ? "application/pdf" : "text/html");
});

app.Run();
