"""CV DevOps Engineer (Docker / Linux / CI-CD)."""
CV = {
    "id": "devops",
    "file": "DevOps",
    "outputs": [("en", "ats"), ("vi", "visual")],

    "title_en": "DevOps Engineer — Docker / Linux / CI-CD",
    "title_vi": "Kỹ sư DevOps — Docker / Linux / CI-CD",
    "badge_en": "DEVOPS ENGINEER",
    "badge_vi": "KỸ SƯ DEVOPS",

    "summary_en": (
        "DevOps-minded engineer with 1.5 years building and running internal platforms at Hoan Cau Group. "
        "Operates multiple systems across three environments (dev / UAT / production) on Docker &amp; Linux: "
        "CI/CD with Gitea Actions, reverse proxy &amp; TLS, monitoring &amp; alerting (Prometheus / "
        "Grafana), scheduled backups and rollback-safe releases. Also develops on the stack (.NET / React), "
        "so tooling and pipelines fit the teams' real needs."
    ),
    "summary_vi": (
        "Kỹ sư thiên về DevOps với 1,5 năm xây dựng và vận hành nền tảng nội bộ tại Tập đoàn Hoàn Cầu. "
        "Vận hành nhiều hệ thống trên 3 môi trường (dev / UAT / production) với Docker &amp; Linux: CI/CD "
        "Gitea Actions, reverse proxy &amp; TLS, giám sát &amp; cảnh báo (Prometheus / Grafana), backup "
        "định kỳ và phát hành có rollback. Đồng thời phát triển trên chính stack đó (.NET / React) nên "
        "pipeline và công cụ sát nhu cầu thực tế của đội."
    ),

    "skills_en": [
        ("Containers &amp; OS:", "Docker, Docker Compose, Linux (Ubuntu), WSL, Bash"),
        ("CI/CD:", "Gitea (self-hosted Git), Gitea Actions pipelines, automated test gates, security scans, "
                   "versioned releases &amp; rollback"),
        ("Networking &amp; edge:", "Nginx, Traefik, Pangolin (reverse proxy / remote access), DNS &amp; TLS, "
                                   "WireGuard (wg-easy) VPN"),
        ("Observability:", "Prometheus, Grafana, Alertmanager, node-exporter; health checks &amp; "
                           "alert design"),
        ("Data operations:", "SQL Server on Docker, scheduled backups &amp; restore drills, capacity &amp; "
                             "cleanup automation"),
        ("Development:", "C# / .NET, React + TypeScript, Python + Gemini API automation"),
    ],
    "skills_vi": [
        ("Container &amp; OS:", "Docker, Docker Compose, Linux (Ubuntu), WSL, Bash"),
        ("CI/CD:", "Gitea (Git tự vận hành), pipeline Gitea Actions, cổng kiểm thử tự động, quét bảo mật, "
                   "phát hành theo version &amp; rollback"),
        ("Mạng &amp; edge:", "Nginx, Traefik, Pangolin (reverse proxy / truy cập từ xa), DNS &amp; TLS, "
                             "VPN WireGuard (wg-easy)"),
        ("Giám sát:", "Prometheus, Grafana, Alertmanager, node-exporter; health check &amp; thiết kế "
                      "cảnh báo"),
        ("Vận hành dữ liệu:", "SQL Server trên Docker, backup định kỳ &amp; diễn tập restore, tự động hóa "
                              "dọn dung lượng"),
        ("Phát triển:", "C# / .NET, React + TypeScript, tự động hóa Python + Gemini API"),
    ],

    "exp_en": [
        "Built and operate the delivery platform for multiple internal systems across <b>three environments "
        "(dev / UAT / production)</b>: Dockerized services, self-hosted registry, CI/CD pipelines in Gitea "
        "Actions (build → test gates → security scan → deploy) with rollback-safe releases.",
        "Run the edge &amp; access layer: reverse proxy (Traefik / Pangolin) with per-application routing "
        "and TLS; SSO-protected internal tools; WireGuard VPN access for branches (region mapping).",
        "Set up observability &amp; reliability: Prometheus + Grafana dashboards and alerts (service health, "
        "data blobs, backups, disk), health checks, scheduled backups with restore drills, incident handling "
        "and capacity cleanup.",
        "Operate SQL Server on Docker for several systems: backup/restore, migration runs and monitoring of "
        "long-running import jobs.",
        "Also develop on the stack (.NET / React) and automate workflows with Python + Gemini API; led the "
        "Base.vn rollout at HCM head office and Khanh Hoa branch.",
    ],
    "exp_vi": [
        "Xây dựng và vận hành nền tảng phát hành cho nhiều hệ thống nội bộ trên <b>3 môi trường "
        "(dev / UAT / production)</b>: dịch vụ đóng gói Docker, registry tự vận hành, pipeline CI/CD trong "
        "Gitea Actions (build → kiểm thử → quét bảo mật → deploy) với phát hành có rollback.",
        "Vận hành tầng edge &amp; truy cập: reverse proxy (Traefik / Pangolin) định tuyến theo ứng dụng và "
        "TLS; công cụ nội bộ bảo vệ bằng SSO; VPN WireGuard cho chi nhánh (ánh xạ theo vùng).",
        "Thiết lập giám sát &amp; độ tin cậy: dashboard và cảnh báo Prometheus + Grafana (sức khỏe dịch vụ, "
        "file dữ liệu, backup, dung lượng), health check, backup định kỳ kèm diễn tập restore, xử lý sự cố "
        "và dọn dung lượng.",
        "Vận hành SQL Server trên Docker cho nhiều hệ thống: backup/restore, chạy migration và theo dõi các "
        "job nhập dữ liệu dài.",
        "Đồng thời phát triển trên stack (.NET / React) và tự động hóa bằng Python + Gemini API; chủ trì "
        "triển khai Base.vn tại hội sở HCM và chi nhánh Khánh Hòa.",
    ],

    "projects_en": [
        ("Delivery platform &amp; environments",
         "Docker · Gitea Actions · Traefik / Pangolin · Linux",
         ["Three-environment release pipeline for multiple systems: build, automated test gates, security "
          "scans, versioned images and rollback.",
          "Self-hosted registry and configuration/secrets management across environments."]),
        ("Observability, backups &amp; VPN",
         "Prometheus · Grafana · Alertmanager · WireGuard",
         ["Dashboards and alerts for service health, blob integrity, backups and disk capacity.",
          "Scheduled SQL Server backups with restore drills; WireGuard VPN (wg-easy) for branch access with "
          "region mapping."]),
        ("Automation &amp; maintenance tooling",
         "Python · Bash · WSL",
         ["Scheduled cleanup and maintenance jobs; Python + Gemini API automations for internal workflows."]),
    ],
    "projects_vi": [
        ("Nền tảng phát hành &amp; môi trường",
         "Docker · Gitea Actions · Traefik / Pangolin · Linux",
         ["Pipeline phát hành 3 môi trường cho nhiều hệ thống: build, cổng kiểm thử tự động, quét bảo mật, "
          "image theo version và rollback.",
          "Registry tự vận hành và quản lý cấu hình/secrets giữa các môi trường."]),
        ("Giám sát, backup &amp; VPN",
         "Prometheus · Grafana · Alertmanager · WireGuard",
         ["Dashboard và cảnh báo cho sức khỏe dịch vụ, toàn vẹn file dữ liệu, backup và dung lượng đĩa.",
          "Backup SQL Server định kỳ kèm diễn tập restore; VPN WireGuard (wg-easy) cho chi nhánh, ánh xạ "
          "theo vùng."]),
        ("Công cụ tự động hóa &amp; bảo trì",
         "Python · Bash · WSL",
         ["Job dọn dẹp &amp; bảo trì định kỳ; tự động hóa quy trình nội bộ bằng Python + Gemini API."]),
    ],
}
