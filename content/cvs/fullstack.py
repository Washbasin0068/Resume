"""CV Full Stack Developer (.NET / React) — bản chính.

Xuất 3 bản: EN (ATS), EN (visual), VI (visual).
"""
CV = {
    "id": "fullstack",
    "file": "FullStack",
    "outputs": [("en", "ats"), ("en", "visual"), ("vi", "visual")],

    "title_en": "Full Stack Developer — .NET / React",
    "title_vi": "Lập trình viên Full Stack — .NET / React",
    "badge_en": "FULL STACK DEVELOPER",
    "badge_vi": "LẬP TRÌNH VIÊN FULL STACK",

    "summary_en": (
        "Full Stack Developer with 1.5 years of hands-on experience building and operating enterprise "
        "platforms at Hoan Cau Group. Delivers end-to-end: .NET (ABP Framework) APIs, React + TypeScript "
        "front-ends, SQL Server data layers, and the Docker/Linux infrastructure with CI/CD and monitoring "
        "they run on. Built a central OpenID Connect sign-on service for five internal applications, and "
        "shipped multi-company reporting and construction-data platforms to production. AI graduate focused "
        "on turning manual business processes into reliable software."
    ),
    "summary_vi": (
        "Lập trình viên Full Stack với 1,5 năm kinh nghiệm xây dựng và vận hành các nền tảng nội bộ tại "
        "Tập đoàn Hoàn Cầu. Làm chủ toàn bộ vòng đời sản phẩm: API .NET (ABP Framework), giao diện React + "
        "TypeScript, SQL Server và hạ tầng Docker/Linux kèm CI/CD, giám sát. Đã xây dựng dịch vụ đăng nhập "
        "tập trung OpenID Connect cho 5 ứng dụng nội bộ; đưa các nền tảng báo cáo và dữ liệu dự án lên "
        "production. Tốt nghiệp ngành Trí tuệ nhân tạo (Đại học Văn Lang)."
    ),

    "skills_en": [
        ("Backend:", "C#, .NET (ASP.NET Core), ABP Framework, Entity Framework Core, REST APIs, "
                     "OpenID Connect / OAuth2 (OpenIddict), RBAC"),
        ("Frontend:", "React, TypeScript, JavaScript, Vite, HTML5, CSS3, responsive web design"),
        ("Databases:", "SQL Server (T-SQL, EF Core migrations), PostgreSQL, data processing (Python, Pandas, NumPy)"),
        ("DevOps &amp; Infra:", "Docker, Docker Compose, Linux, WSL, Git / Gitea, CI/CD (Gitea Actions), "
                                "Nginx, Traefik / Pangolin, Prometheus &amp; Grafana, backup &amp; restore, Bash"),
        ("AI &amp; Automation:", "Gemini API integration, Python automation, workflow optimisation"),
        ("Testing:", "xUnit, Vitest, Playwright (automated CI gates)"),
    ],
    "skills_vi": [
        ("Backend:", "C#, .NET (ASP.NET Core), ABP Framework, Entity Framework Core, REST API, "
                     "OpenID Connect / OAuth2 (OpenIddict), RBAC"),
        ("Frontend:", "React, TypeScript, JavaScript, Vite, HTML5, CSS3, giao diện responsive"),
        ("Cơ sở dữ liệu:", "SQL Server (T-SQL, EF Core migrations), PostgreSQL, xử lý dữ liệu (Python, Pandas, NumPy)"),
        ("DevOps &amp; Hạ tầng:", "Docker, Docker Compose, Linux, WSL, Git / Gitea, CI/CD (Gitea Actions), "
                                  "Nginx, Traefik / Pangolin, Prometheus &amp; Grafana, backup &amp; restore, Bash"),
        ("AI &amp; Tự động hóa:", "Tích hợp Gemini API, tự động hóa bằng Python, tối ưu quy trình"),
        ("Kiểm thử:", "xUnit, Vitest, Playwright (cổng kiểm thử tự động trong CI)"),
    ],

    "exp_en": [
        "<b>Full-stack development:</b> Designed and built internal platforms end-to-end — ABP Framework "
        "(.NET / C#) APIs, React + TypeScript UIs and SQL Server — including a <b>group financial &amp; fund "
        "reporting platform</b> (period-based reporting for 44 companies: MISA ledger import &amp; validation, "
        "multi-company approval workflows, dashboards) and a <b>construction project data platform</b>, "
        "both shipped to production.",
        "<b>Identity &amp; SSO:</b> Built a centralised <b>OpenID Connect (OpenIddict)</b> sign-on service "
        "for <b>5 internal applications</b>: authorization-code + PKCE for SPAs, client-credentials service "
        "scopes, role-based access, per-application catalogue &amp; policies, session/location tracking by "
        "region, audit logs and an admin console.",
        "<b>DevOps &amp; delivery:</b> Own the release pipeline of all systems across <b>three environments "
        "(dev / UAT / production)</b>: Docker &amp; Linux, CI/CD with Gitea Actions (build, automated test "
        "gates, security scans), reverse proxy (Traefik / Pangolin), Prometheus/Grafana alerting, scheduled "
        "backups and rollback-safe releases.",
        "<b>AI &amp; automation:</b> Automated internal data workflows with Python (WSL) + Gemini API, "
        "removing repetitive manual processing for management teams.",
        "<b>Digital transformation:</b> Led the Base.vn rollout at the <b>HCM head office and Khanh Hoa "
        "branch</b>; tracked project milestones and reported progress directly to the Board of Directors.",
    ],
    "exp_vi": [
        "<b>Phát triển Full Stack:</b> Thiết kế và xây dựng nền tảng nội bộ trọn gói — API ABP Framework "
        "(.NET / C#), giao diện React + TypeScript, SQL Server — gồm <b>nền tảng báo cáo tài chính &amp; quỹ "
        "tập đoàn</b> (báo cáo theo kỳ cho 44 công ty: nhập &amp; kiểm tra sổ MISA, quy trình duyệt đa công "
        "ty, dashboard) và <b>nền tảng dữ liệu dự án xây dựng</b>, cả hai đã lên production.",
        "<b>Định danh &amp; SSO:</b> Xây dựng dịch vụ đăng nhập tập trung <b>OpenID Connect (OpenIddict)</b> "
        "cho <b>5 ứng dụng nội bộ</b>: authorization-code + PKCE cho SPA, client-credentials cho service, "
        "phân quyền theo vai trò, danh mục &amp; chính sách truy cập theo ứng dụng, theo dõi phiên theo vùng, "
        "nhật ký kiểm toán và màn quản trị.",
        "<b>DevOps &amp; phát hành:</b> Quản lý quy trình phát hành toàn bộ hệ thống trên <b>3 môi trường "
        "(dev / UAT / production)</b>: Docker &amp; Linux, CI/CD với Gitea Actions (build, cổng kiểm thử tự "
        "động, quét bảo mật), reverse proxy (Traefik / Pangolin), cảnh báo Prometheus/Grafana, backup định "
        "kỳ, phát hành có rollback.",
        "<b>AI &amp; tự động hóa:</b> Tự động hóa xử lý dữ liệu nội bộ bằng Python (WSL) + Gemini API, giảm "
        "việc thủ công lặp lại cho bộ phận quản lý.",
        "<b>Chuyển đổi số:</b> Chủ trì triển khai Base.vn tại <b>hội sở HCM và chi nhánh Khánh Hòa</b>; theo "
        "dõi tiến độ dự án và báo cáo trực tiếp Ban Tổng Giám đốc.",
    ],

    "projects_en": [
        ("Group financial &amp; fund reporting platform",
         "ABP / .NET · React · TypeScript · SQL Server · Docker",
         ["Period-based reporting for <b>44 companies</b>: MISA ledger import &amp; validation, approval "
          "workflows and dashboards for accounting teams.",
          "Three-environment delivery with automated tests, health checks, monitoring and backup/restore "
          "procedures."]),
        ("Central SSO &amp; identity service",
         "ABP / .NET · OpenIddict / OIDC · SQL Server · Docker",
         ["Single sign-on and application catalogue for <b>5 internal applications</b>; admin console for "
          "users, roles, sessions and audit history; access policies &amp; alerts.",
          "Service-to-service APIs (user lookup, application members) for access verification and "
          "synchronisation across systems."]),
        ("Construction project data platform",
         "ABP / .NET · React · TypeScript · Docker",
         ["Investor-side project data: coordination workspace, member invitations and master-data "
          "synchronisation; released to production."]),
    ],
    "projects_vi": [
        ("Nền tảng báo cáo tài chính &amp; quỹ tập đoàn",
         "ABP / .NET · React · TypeScript · SQL Server · Docker",
         ["Báo cáo theo kỳ cho <b>44 công ty</b>: nhập &amp; kiểm tra sổ MISA, quy trình duyệt, dashboard "
          "cho khối kế toán.",
          "Vận hành 3 môi trường với kiểm thử tự động, health check, giám sát và quy trình backup/restore."]),
        ("Dịch vụ định danh &amp; SSO tập trung",
         "ABP / .NET · OpenIddict / OIDC · SQL Server · Docker",
         ["SSO và danh mục ứng dụng cho <b>5 ứng dụng nội bộ</b>; màn quản trị người dùng/vai trò/phiên/"
          "nhật ký; chính sách &amp; cảnh báo truy cập.",
          "API dịch vụ (tra cứu người dùng, thành viên ứng dụng) cho các hệ thống khác xác minh và đồng bộ "
          "quyền truy cập."]),
        ("Nền tảng dữ liệu dự án xây dựng",
         "ABP / .NET · React · TypeScript · Docker",
         ["Dữ liệu dự án phía chủ đầu tư: không gian điều phối, mời thành viên, đồng bộ Master Data; "
          "đã phát hành production."]),
    ],

    "soft_skills_en": [
        "Self-learning &amp; adaptable",
        "Teamwork &amp; collaboration",
        "Technical problem-solving",
        "Clear written communication",
    ],
    "soft_skills_vi": [
        "Tự học &amp; thích nghi nhanh",
        "Làm việc nhóm",
        "Giải quyết vấn đề kỹ thuật",
        "Viết tài liệu rõ ràng",
    ],
}
