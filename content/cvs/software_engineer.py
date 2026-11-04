"""CV Software Engineer (tổng quát — full stack & platform)."""
CV = {
    "id": "software-engineer",
    "file": "SoftwareEngineer",
    "outputs": [("en", "ats"), ("vi", "visual")],

    "title_en": "Software Engineer — Full Stack &amp; Platform",
    "title_vi": "Kỹ sư phần mềm — Full Stack &amp; Nền tảng",
    "badge_en": "SOFTWARE ENGINEER",
    "badge_vi": "KỸ SƯ PHẦN MỀM",

    "summary_en": (
        "Software Engineer with 1.5 years of hands-on experience delivering and operating enterprise "
        "platforms at Hoan Cau Group. Works across the stack: C#/.NET (ABP Framework) APIs, React + "
        "TypeScript front-ends, SQL Server, and the Docker/Linux infrastructure with CI/CD and monitoring. "
        "Built a central OpenID Connect sign-on service for five internal applications and shipped "
        "multi-company reporting and project-data platforms to production. AI graduate; automates workflows "
        "with Python + Gemini API."
    ),
    "summary_vi": (
        "Kỹ sư phần mềm với 1,5 năm kinh nghiệm xây dựng và vận hành nền tảng nội bộ tại Tập đoàn Hoàn Cầu. "
        "Làm việc xuyên suốt stack: API C#/.NET (ABP Framework), giao diện React + TypeScript, SQL Server và "
        "hạ tầng Docker/Linux kèm CI/CD, giám sát. Đã xây dựng dịch vụ đăng nhập tập trung OpenID Connect "
        "cho 5 ứng dụng nội bộ; đưa nền tảng báo cáo đa công ty và nền tảng dữ liệu dự án lên production. "
        "Tốt nghiệp AI; tự động hóa bằng Python + Gemini API."
    ),

    "skills_en": [
        ("Languages:", "C#, TypeScript / JavaScript, Python, SQL (T-SQL), Bash"),
        ("Frameworks:", ".NET (ASP.NET Core), ABP Framework, React, Entity Framework Core, REST APIs, Vite"),
        ("Auth &amp; Data:", "OpenID Connect / OAuth2 (OpenIddict), RBAC, SQL Server, PostgreSQL, "
                             "Pandas / NumPy"),
        ("Infrastructure:", "Docker, Docker Compose, Linux, WSL, Git / Gitea, CI/CD (Gitea Actions), Nginx, "
                            "Traefik / Pangolin, Prometheus &amp; Grafana, backup &amp; restore"),
        ("Practices:", "Automated testing (xUnit, Vitest, Playwright), code review, technical documentation, "
                       "rollback-safe releases"),
        ("AI &amp; Automation:", "Gemini API integration, Python automation, workflow optimisation"),
    ],
    "skills_vi": [
        ("Ngôn ngữ:", "C#, TypeScript / JavaScript, Python, SQL (T-SQL), Bash"),
        ("Framework:", ".NET (ASP.NET Core), ABP Framework, React, Entity Framework Core, REST API, Vite"),
        ("Xác thực &amp; Dữ liệu:", "OpenID Connect / OAuth2 (OpenIddict), RBAC, SQL Server, PostgreSQL, "
                                    "Pandas / NumPy"),
        ("Hạ tầng:", "Docker, Docker Compose, Linux, WSL, Git / Gitea, CI/CD (Gitea Actions), Nginx, "
                     "Traefik / Pangolin, Prometheus &amp; Grafana, backup &amp; restore"),
        ("Quy trình:", "Kiểm thử tự động (xUnit, Vitest, Playwright), review code, viết tài liệu, "
                       "phát hành có rollback"),
        ("AI &amp; Tự động hóa:", "Tích hợp Gemini API, tự động hóa bằng Python, tối ưu quy trình"),
    ],

    "exp_en": [
        "Delivered internal platforms end-to-end — .NET (ABP Framework) APIs, React + TypeScript UIs and "
        "SQL Server — including a <b>multi-company financial reporting platform</b> (44 companies: MISA "
        "ledger import &amp; validation, approval workflows, dashboards) and a <b>construction project data "
        "platform</b>, both in production.",
        "Built a central <b>OpenID Connect (OpenIddict)</b> sign-on service for <b>5 internal "
        "applications</b>: SPA flows with PKCE, client-credentials service scopes, role-based access, "
        "per-application catalogue &amp; policies, session/location tracking, audit logs and an admin console.",
        "Operate the full delivery pipeline across <b>three environments (dev / UAT / production)</b>: "
        "Docker &amp; Linux, CI/CD with Gitea Actions (build, automated test gates, security scans), reverse "
        "proxy (Traefik / Pangolin), Prometheus/Grafana alerting, scheduled backups and rollback-safe "
        "releases.",
        "Automate internal data workflows with Python (WSL) + Gemini API, removing repetitive manual "
        "processing for management teams.",
        "Led the Base.vn rollout at the <b>HCM head office and Khanh Hoa branch</b>; tracked project "
        "milestones and reported progress directly to the Board of Directors.",
    ],
    "exp_vi": [
        "Xây dựng nền tảng nội bộ trọn gói — API .NET (ABP Framework), giao diện React + TypeScript, SQL "
        "Server — gồm <b>nền tảng báo cáo tài chính đa công ty</b> (44 công ty: nhập &amp; kiểm tra sổ MISA, "
        "quy trình duyệt, dashboard) và <b>nền tảng dữ liệu dự án xây dựng</b>, cả hai đã lên production.",
        "Xây dựng dịch vụ đăng nhập tập trung <b>OpenID Connect (OpenIddict)</b> cho <b>5 ứng dụng nội "
        "bộ</b>: luồng SPA với PKCE, client-credentials cho service, phân quyền theo vai trò, danh mục &amp; "
        "chính sách theo ứng dụng, theo dõi phiên theo vùng, nhật ký kiểm toán và màn quản trị.",
        "Vận hành quy trình phát hành trên <b>3 môi trường (dev / UAT / production)</b>: Docker &amp; Linux, "
        "CI/CD với Gitea Actions (build, cổng kiểm thử tự động, quét bảo mật), reverse proxy (Traefik / "
        "Pangolin), cảnh báo Prometheus/Grafana, backup định kỳ, phát hành có rollback.",
        "Tự động hóa xử lý dữ liệu nội bộ bằng Python (WSL) + Gemini API, giảm việc thủ công lặp lại cho "
        "bộ phận quản lý.",
        "Chủ trì triển khai Base.vn tại <b>hội sở HCM và chi nhánh Khánh Hòa</b>; theo dõi tiến độ dự án "
        "và báo cáo trực tiếp Ban Tổng Giám đốc.",
    ],

    "projects_en": [
        ("Multi-company financial &amp; fund reporting platform",
         "ABP / .NET · React · TypeScript · SQL Server · Docker",
         ["Period-based reporting for <b>44 companies</b>: MISA ledger import &amp; validation, approval "
          "workflows, dashboards for accounting teams.",
          "Three-environment delivery with automated tests, health checks, monitoring and backup/restore."]),
        ("Central SSO &amp; identity service",
         "ABP / .NET · OpenIddict / OIDC · SQL Server · Docker",
         ["Single sign-on and application catalogue for <b>5 internal applications</b>; admin console for "
          "users, roles, sessions and audit history.",
          "Service-to-service APIs (user lookup, application members) for access verification and sync."]),
        ("Construction project data platform",
         "ABP / .NET · React · TypeScript · Docker",
         ["Investor-side project data: coordination workspace, member invitations and master-data "
          "synchronisation; released to production."]),
    ],
    "projects_vi": [
        ("Nền tảng báo cáo tài chính &amp; quỹ đa công ty",
         "ABP / .NET · React · TypeScript · SQL Server · Docker",
         ["Báo cáo theo kỳ cho <b>44 công ty</b>: nhập &amp; kiểm tra sổ MISA, quy trình duyệt, dashboard "
          "cho khối kế toán.",
          "Vận hành 3 môi trường với kiểm thử tự động, health check, giám sát và backup/restore."]),
        ("Dịch vụ định danh &amp; SSO tập trung",
         "ABP / .NET · OpenIddict / OIDC · SQL Server · Docker",
         ["SSO và danh mục ứng dụng cho <b>5 ứng dụng nội bộ</b>; màn quản trị người dùng/vai trò/phiên/"
          "nhật ký.",
          "API dịch vụ (tra cứu người dùng, thành viên ứng dụng) để xác minh và đồng bộ quyền truy cập."]),
        ("Nền tảng dữ liệu dự án xây dựng",
         "ABP / .NET · React · TypeScript · Docker",
         ["Dữ liệu dự án phía chủ đầu tư: không gian điều phối, mời thành viên, đồng bộ Master Data; "
          "đã phát hành production."]),
    ],
}
