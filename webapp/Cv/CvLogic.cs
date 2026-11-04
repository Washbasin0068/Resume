using System.Diagnostics;
using System.IO.Compression;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml.Linq;

namespace VietCv;

/// <summary>Chọn nội dung khớp role/JD, kiểm tra an toàn, trích văn bản CV tải lên.</summary>
public static partial class CvLogic
{
    public static readonly string[] Diacritics = "ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ".Select(c => c.ToString()).ToArray();

    public static bool Has(string text, string word) =>
        Regex.IsMatch(text, $@"(?<![\w]){Regex.Escape(word)}(?![\w])", RegexOptions.IgnoreCase);

    /// <summary>Chuỗi hoặc {"en":..,"vi":..} -> chuỗi.</summary>
    public static string Tx(Dictionary<string, string>? d, string lang, string fallback = "")
    {
        if (d is null || d.Count == 0) return fallback;
        return d.TryGetValue(lang, out var v) ? v : d.GetValueOrDefault("en", fallback);
    }

    /// <summary>Văn bản thuần -> HTML an toàn; **x** -> &lt;b&gt;x&lt;/b&gt;.</summary>
    public static string Esc(string? text)
    {
        var s = System.Net.WebUtility.HtmlEncode(text ?? "");
        return Regex.Replace(s, @"\*\*(.+?)\*\*", "<b>$1</b>");
    }

    public static string Slug(string s)
    {
        var normalized = s.Normalize(NormalizationForm.FormD);
        var sb = new StringBuilder();
        foreach (var ch in normalized)
        {
            if (System.Globalization.CharUnicodeInfo.GetUnicodeCategory(ch) == System.Globalization.UnicodeCategory.NonSpacingMark) continue;
            sb.Append(ch is 'đ' ? 'd' : ch is 'Đ' ? 'D' : ch);
        }
        var ascii = Regex.Replace(sb.ToString(), "[^A-Za-z0-9]+", "");
        if (ascii.Length == 0) return "Role";
        return char.ToUpperInvariant(ascii[0]) + ascii[1..];
    }

    public static (Dictionary<string, int> Tags, List<string> Matched, List<string> Gaps) Analyze(
        Profile p, Taxonomy tax, string role, string jd)
    {
        var roleL = role.ToLowerInvariant();
        var jdL = jd.ToLowerInvariant();
        var both = roleL + "\n" + jdL;
        var tags = new Dictionary<string, int>();
        foreach (var (tag, words) in tax.Aliases)
        {
            var n = words.Sum(w => (Has(roleL, w) ? 3 : 0) + (Has(jdL, w) ? Math.Min(2, Regex.Matches(jdL, Regex.Escape(w)).Count) : 0));
            if (n > 0) tags[tag] = n;
        }
        if (tags.Count == 0) tags["fullstack"] = 3;
        var matched = new List<string>();
        var known = new HashSet<string>(StringComparer.OrdinalIgnoreCase);
        foreach (var g in p.Skills)
        foreach (var it in g.Items)
        {
            var ms = it.M is { Count: > 0 } ? it.M : new List<string> { it.N.ToLowerInvariant() };
            foreach (var m in ms) known.Add(m);
            if (ms.Any(m => Has(both, m))) matched.Add(it.N);
        }
        var gaps = tax.Watchlist.Where(w => Has(both, w) && !known.Contains(w)).Distinct().ToList();
        return (tags, matched, gaps);
    }

    /// <summary>Tự gắn tag + trọng số cho mục người dùng nhập tay (không có tag).</summary>
    public static Profile AutoTag(Profile p, Taxonomy tax)
    {
        foreach (var e in p.Experience)
        {
            if (e.W == 0) e.W = 2;
            if (e.T.Count == 0) e.T = Guess(e.Text.GetValueOrDefault("en", "") + " " + e.Text.GetValueOrDefault("vi", ""), tax);
        }
        foreach (var x in p.Projects)
        {
            if (x.W == 0) x.W = 2;
            if (x.T.Count == 0) x.T = Guess(x.N.GetValueOrDefault("en", "") + " " + x.Tech + " " + x.En + " " + x.Vi, tax);
        }
        foreach (var g in p.Skills)
        foreach (var i in g.Items)
            if (i.T.Count == 0) i.T = Guess(i.N, tax);
        return p;
    }

    private static List<string> Guess(string text, Taxonomy tax) =>
        tax.Aliases.Where(a => a.Value.Any(w => Has(text, w))).Select(a => a.Key).Take(4).ToList() is { Count: > 0 } tags
            ? tags : new List<string> { "fullstack" };

    public static int Score(object item, Dictionary<string, int> tags, List<string> t, string text, int w = 0, IEnumerable<string>? m = null)
    {
        var s = w + t.Sum(tag => tags.GetValueOrDefault(tag));
        if (m is not null && m.Any(x => !string.IsNullOrEmpty(x) && Has(text, x))) s += 8;
        return s;
    }

    public static (List<Experience> Exp, List<ProjectItem> Proj, List<(SkillGroup G, List<Skill> Items)> Groups) Pick(
        Profile p, Taxonomy tax, string role, string jd, int limitExp = 7, int limitProj = 3, int groupItems = 8, int groups = 7)
    {
        var (tags, _, _) = Analyze(p, tax, role, jd);
        var both = role.ToLowerInvariant() + "\n" + jd.ToLowerInvariant();
        var exp = p.Experience
            .Select(e => (S: Score(e, tags, e.T, both, e.W), E: e))
            .OrderByDescending(x => x.S).Take(limitExp).Select(x => x.E).ToList();
        var proj = p.Projects
            .Select(x => (S: Score(x, tags, x.T, both, x.W), P: x))
            .OrderByDescending(x => x.S).Take(limitProj).Select(x => x.P).ToList();
        var gs = p.Skills.Select(g =>
        {
            var its = g.Items.Select(i => (S: Score(i, tags, i.T, both, 0, i.M), I: i))
                .OrderByDescending(x => x.S).Take(groupItems).ToList();
            if (its.Count > 3) its = its.Where(x => x.S > 0).ToList();
            return (Sum: its.Sum(x => x.S), G: g, Items: its.Select(x => x.I).ToList());
        }).Where(x => x.Items.Count > 0).OrderByDescending(x => x.Sum).Take(groups).ToList();
        return (exp, proj, gs.Select(x => (x.G, x.Items)).ToList());
    }

    /// <summary>Bỏ phần điểm thấp nhất để vừa 1 trang. False nếu hết.</summary>
    public static bool Trim(List<Experience> exp, List<ProjectItem> proj, List<(SkillGroup G, List<Skill> Items)> groups)
    {
        if (exp.Count > 4) { exp.RemoveAt(exp.Count - 1); return true; }
        if (proj.Count > 2) { proj.RemoveAt(proj.Count - 1); return true; }
        if (exp.Count > 3) { exp.RemoveAt(exp.Count - 1); return true; }
        var g = groups.Where(x => x.Items.Count > 1).OrderByDescending(x => x.Items.Count).FirstOrDefault();
        if (g.G is null) return false;
        g.Items.RemoveAt(g.Items.Count - 1);
        return true;
    }

    public static List<string> Leaks(string htmlText, IEnumerable<string> words)
    {
        var text = Regex.Replace(System.Net.WebUtility.HtmlDecode(Regex.Replace(htmlText, "<[^>]+>", " ")), @"\s+", " ").ToLowerInvariant();
        return words.Where(w => !string.IsNullOrWhiteSpace(w) && Has(text, w.Trim())).ToList();
    }

    /// <summary>Các từ tiếng Việt có dấu trong HTML mà text PDF không có (lỗi font).</summary>
    public static List<string> MissingGlyphs(string htmlText, string pdfPath)
    {
        var txt = PdfToText(pdfPath);
        if (txt is null) return new();
        var body = Regex.Replace(System.Net.WebUtility.HtmlDecode(
            Regex.Replace(htmlText.Split("<body").LastOrDefault() ?? "", "<[^>]+>", " ")), @"\s+", " ");
        var words = Regex.Matches(body.ToLowerInvariant(), @"[^\W_]+").Select(m => m.Value)
            .Where(w => w.Any(c => Diacritics.Contains(c.ToString()))).Distinct();
        var pdf = txt.ToLowerInvariant();
        return words.Where(w => !pdf.Contains(w)).ToList();
    }

    public static string? PdfToText(string pdfPath) => Run("pdftotext", $"\"{pdfPath}\" -");

    public static string? Run(string file, string args, int timeoutMs = 120000)
    {
        try
        {
            var psi = new ProcessStartInfo(file, args) { RedirectStandardOutput = true, RedirectStandardError = true, UseShellExecute = false };
            using var proc = Process.Start(psi)!;
            var output = proc.StandardOutput.ReadToEnd();
            proc.StandardError.ReadToEnd();
            if (!proc.WaitForExit(timeoutMs)) { proc.Kill(true); return null; }
            return proc.ExitCode == 0 ? output : null;
        }
        catch (Exception) { return null; }
    }

    // ------------------------------------------------------- trích CV tải lên
    public static ImproveResult Improve(string fileName, byte[] bytes, Profile profile, Taxonomy tax)
    {
        var text = ExtractText(fileName, bytes);
        return new ImproveResult { Text = text, Chars = text.Length, Findings = FindIssues(text, profile, tax) };
    }

    public static string ExtractText(string fileName, byte[] bytes)
    {
        var ext = Path.GetExtension(fileName).ToLowerInvariant();
        if (ext is ".txt" or ".md" or ".markdown") return Encoding.UTF8.GetString(bytes);
        if (ext == ".docx") return DocxText(bytes);
        if (ext == ".pdf") return PdfText(bytes) ?? throw new InvalidOperationException(
            "Không đọc được PDF (cần poppler-utils trong máy chủ). Hãy dán nội dung vào form.");
        throw new InvalidOperationException("Chỉ nhận .pdf, .docx, .txt, .md");
    }

    private static string DocxText(byte[] bytes)
    {
        using var zip = new ZipArchive(new MemoryStream(bytes), ZipArchiveMode.Read);
        var entry = zip.GetEntry("word/document.xml") ?? throw new InvalidOperationException("File .docx không hợp lệ");
        using var s = entry.Open();
        var doc = XDocument.Load(s);
        XNamespace w = "http://schemas.openxmlformats.org/wordprocessingml/2006/main";
        var paragraphs = doc.Descendants(w + "p").Select(p => string.Concat(p.Descendants(w + "t").Select(t => t.Value)));
        return string.Join("\n", paragraphs).Trim();
    }

    private static string? PdfText(byte[] bytes)
    {
        var tmp = Path.Combine(Path.GetTempPath(), $"cv-{Guid.NewGuid():N}.pdf");
        File.WriteAllBytes(tmp, bytes);
        try { return PdfToText(tmp); }
        finally { File.Delete(tmp); }
    }

    public static List<Finding> FindIssues(string text, Profile p, Taxonomy tax)
    {
        var f = new List<Finding>();
        var low = text.ToLowerInvariant();
        void Add(string level, string msg) => f.Add(new Finding { Level = level, Message = msg });
        if (text.Length < 300) Add("warn", "Văn bản trích ra quá ngắn — có thể là CV dạng ảnh (scan). Hãy dán nội dung bằng tay.");
        if (!low.Contains('@') && !Regex.IsMatch(text, @"\d{3}[ .-]?\d{3}[ .-]?\d{3,}"))
            Add("warn", "Không thấy email/số điện thoại. Nhà tuyển dụng cần liên hệ được.");
        // Mỗi mục có nhiều cách gọi (EN/VI) — chỉ báo thiếu khi không có cách gọi nào.
        foreach (var (aliases, name) in new[]
                 {
                     (new[] { "kinh nghiệm", "experience" }, "experience"),
                     (new[] { "kỹ năng", "skills" }, "skills"),
                     (new[] { "học vấn", "education" }, "education"),
                 })
            if (!aliases.Any(low.Contains))
                Add("warn", $"Thiếu mục '{name}'. ATS thường chấm điểm theo mục chuẩn.");
        if (low.Contains("responsible for")) Add("info", "Đổi 'responsible for' sang động từ mạnh: Built, Designed, Cut, Automated.");
        foreach (var bad in new[] { "team player", "hard-working", "nhiệt tình", "chăm chỉ", "dynamic" })
            if (low.Contains(bad)) Add("info", $"Bỏ sáo ngữ '{bad}' — thay bằng kết quả cụ thể.");
        var leaks = Leaks(text, p.Denylist ?? new());
        foreach (var l in leaks) Add("risk", $"Có thể lộ thông tin nội bộ: '{l}'. Bỏ hoặc viết chung hơn.");
        var numbers = Regex.Matches(text, @"\d+\s?%").Count;
        if (numbers == 0) Add("info", "Chưa có con số %. Thêm kết quả đo được (thời gian, %, số lượng dạng khoảng).");
        var bullets = text.Split('\n').Select(l => l.Trim()).Where(l => l.StartsWith('-') || l.StartsWith('•')).ToList();
        var longOnes = bullets.Count(b => b.Length > 220);
        if (longOnes > 0) Add("info", $"{longOnes} gạch đầu dòng quá dài (>220 ký tự). Mỗi dòng nên dưới 2 dòng giấy.");
        foreach (var w in tax.Watchlist.Where(w => Hack(low, w)).Take(8))
            Add("info", $"JD/ngân hàng có '{w}' nhưng CV chưa nhắc — chỉ thêm nếu bạn thật sự biết.");
        return f;
    }

    private static bool Hack(string text, string word) => Has(text, word);
}
