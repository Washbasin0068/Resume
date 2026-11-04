using System.Diagnostics;
using System.Text.RegularExpressions;

namespace VietCv;

/// <summary>HTML -> PDF bằng Chromium headless (không cần thư viện ngoài).</summary>
public static class Pdf
{
    public static string Chrome()
    {
        var env = Environment.GetEnvironmentVariable("CHROME");
        if (!string.IsNullOrWhiteSpace(env)) return env;
        foreach (var n in new[] { "chromium", "chromium-browser", "google-chrome", "chrome" })
        {
            var path = Which(n);
            if (path is not null) return path;
        }
        var home = Environment.GetFolderPath(Environment.SpecialFolder.UserProfile);
        var cache = Path.Combine(home, ".cache", "ms-playwright");
        if (Directory.Exists(cache))
            foreach (var d in Directory.GetDirectories(cache, "chromium-*").OrderByDescending(x => x))
            {
                var hit = Directory.GetFiles(d, "chrome", SearchOption.AllDirectories).FirstOrDefault();
                if (hit is not null) return hit;
            }
        return "chromium";
    }

    private static string? Which(string name)
    {
        foreach (var dir in (Environment.GetEnvironmentVariable("PATH") ?? "").Split(Path.PathSeparator))
        {
            if (string.IsNullOrWhiteSpace(dir)) continue;
            var p = Path.Combine(dir, name);
            if (File.Exists(p)) return p;
        }
        return null;
    }

    /// <summary>In PDF, trả về số trang (0 = không đọc được).</summary>
    public static int Print(string htmlPath, string pdfPath)
    {
        var psi = new ProcessStartInfo(Chrome())
        {
            RedirectStandardError = true,
            RedirectStandardOutput = true,
            UseShellExecute = false,
        };
        foreach (var a in new[]
                 {
                     "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
                     "--no-first-run", "--no-default-browser-check", "--disable-extensions",
                     "--disable-background-networking", "--disable-component-update", "--disable-sync",
                     $"--print-to-pdf={pdfPath}", new Uri(htmlPath).AbsoluteUri,
                 })
            psi.ArgumentList.Add(a);
        using var proc = Process.Start(psi) ?? throw new InvalidOperationException("Không chạy được Chromium");
        proc.StandardOutput.ReadToEnd();
        var err = proc.StandardError.ReadToEnd();
        if (!proc.WaitForExit(120000)) { proc.Kill(true); throw new TimeoutException("Chromium quá lâu"); }
        // Chromium hay ghi rác ra stderr và trả mã khác 0 dù đã in xong -> chỉ tin vào file.
        if (!File.Exists(pdfPath) || new FileInfo(pdfPath).Length == 0)
            throw new InvalidOperationException("Chromium không in được PDF: " +
                string.Join(" | ", err.Trim().Split('\n').TakeLast(2)));
        return Pages(pdfPath);
    }

    public static int Pages(string pdfPath)
    {
        var outp = CvLogic.Run("pdfinfo", $"\"{pdfPath}\"");
        if (outp is null) return 0;
        var m = Regex.Match(outp, @"^Pages:\s+(\d+)", RegexOptions.Multiline);
        return m.Success ? int.Parse(m.Groups[1].Value) : 0;
    }
}
