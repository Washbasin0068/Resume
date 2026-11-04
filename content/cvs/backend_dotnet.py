"""CV Backend Developer (.NET / C#)."""
CV = {
    "id": "backend-dotnet",
    "file": "BackendDotNet",
    "outputs": [("en", "ats"), ("vi", "visual")],

    "title_en": "Backend Developer — .NET / C#",
    "title_vi": "Lập trình viên Backend — .NET / C#",
    "badge_en": "BACKEND DEVELOPER",
    "badge_vi": "LẬP TRÌNH VIÊN BACKEND",

    "summary_en": (
        "Backend-focused developer with 1.5 years building .NET services at Hoan Cau Group. Designs and "
        "ships APIs with ABP Framework / ASP.NET Core, Entity Framework Core and SQL Server — including "
        "data-heavy import &amp; validation pipelines and multi-company approval workflows. Strong on "
        "authentication &amp; authorization (OpenID Connect / OpenIddict, OAuth2 client credentials, RBAC) "
        "and system-to-system integrations; operates what is built with Docker, CI/CD and monitoring."
    ),
    "summary_vi": (
        "Lập trình viên thiên về backend với 1,5 năm xây dựng dịch vụ .NET tại Tập đoàn Hoàn Cầu. Thiết kế "
        "và phát triển API với ABP Framework / ASP.NET Core, Entity Framework Core và SQL Server — gồm các "
        "pipeline nhập &amp; kiểm tra dữ liệu nặng và quy trình duyệt đa công ty. Mạnh về xác thực &amp; "
        "phân quyền (OpenID Connect / OpenIddict, OAuth2 client credentials, RBAC) và tích hợp hệ thống; "
        "vận hành sản phẩm với Docker, CI/CD và giám sát."
    ),

    "skills_en": [
        ("Backend:", "C#, .NET (ASP.NET Core), ABP Framework, Entity Framework Core, REST APIs, "
                     "validation &amp; import pipelines"),
        ("Auth &amp; Security:", "OpenID Connect / OAuth2 (OpenIddict), authorization-code + PKCE, "
                                 "client credentials, RBAC, audit logging"),
        ("Data:", "SQL Server (T-SQL, schema design, EF Core migrations), PostgreSQL, data validation, "
                  "Python (Pandas, NumPy)"),
        ("Integration:", "Service-to-service APIs, master-data synchronisation, webhooks, user lookup APIs"),
        ("Quality &amp; Ops:", "xUnit, CI test gates &amp; security scans, Docker, Linux, Gitea Actions "
                               "CI/CD, Prometheus / Grafana"),
        ("Secondary:", "React + TypeScript, Python + Gemini API automation"),
    ],
    "skills_vi": [
        ("Backend:", "C#, .NET (ASP.NET Core), ABP Framework, Entity Framework Core, REST API, "
                     "pipeline nhập &amp; kiểm tra dữ liệu"),
        ("Xác thực &amp; Bảo mật:", "OpenID Connect / OAuth2 (OpenIddict), authorization-code + PKCE, "
                                    "client credentials, RBAC, nhật ký kiểm toán"),
        ("Dữ liệu:", "SQL Server (T-SQL, thiết kế schema, EF Core migrations), PostgreSQL, kiểm tra dữ "
                     "liệu, Python (Pandas, NumPy)"),
        ("Tích hợp:", "API service-to-service, đồng bộ Master Data, webhook, API tra cứu người dùng"),
        ("Chất lượng &amp; Vận hành:", "xUnit, cổng kiểm thử &amp; quét bảo mật trong CI, Docker, Linux, "
                                       "Gitea Actions CI/CD, Prometheus / Grafana"),
        ("Bổ trợ:", "React + TypeScript, tự động hóa Python + Gemini API"),
    ],

    "exp_en": [
        "Designed and shipped .NET APIs for two production platforms: a <b>multi-company financial "
        "reporting platform</b> (44 companies — MISA ledger import &amp; validation, approval workflows) "
        "and a <b>construction project data platform</b> (coordination, member invitations, master-data "
        "sync).",
        "Built the domain, data and API layers: ABP Framework modules, EF Core + SQL Server schemas and "
        "migrations, REST endpoints consumed by React SPAs and other systems.",
        "Implemented authentication &amp; access control: central <b>OIDC / OpenIddict</b> service "
        "(authorization-code + PKCE, client-credentials service scopes), role-based access, "
        "per-application policies, session/audit tracking and admin APIs.",
        "Delivered integrations: service-to-service APIs (user lookup, application members) and "
        "master-data synchronisation between internal systems.",
        "Own quality &amp; operations: xUnit tests wired into CI, Dockerized deployments across "
        "dev / UAT / production, monitoring and backups; automate workflows with Python + Gemini API.",
    ],
    "exp_vi": [
        "Thiết kế và phát triển API .NET cho hai nền tảng production: <b>nền tảng báo cáo tài chính đa "
        "công ty</b> (44 công ty — nhập &amp; kiểm tra sổ MISA, quy trình duyệt) và <b>nền tảng dữ liệu dự "
        "án xây dựng</b> (điều phối, mời thành viên, đồng bộ Master Data).",
        "Xây dựng tầng domain, dữ liệu và API: module ABP Framework, schema &amp; migration EF Core + SQL "
        "Server, REST endpoint cho SPA React và các hệ thống khác.",
        "Triển khai xác thực &amp; phân quyền: dịch vụ <b>OIDC / OpenIddict</b> tập trung "
        "(authorization-code + PKCE, client-credentials cho service), phân quyền theo vai trò, chính sách "
        "theo ứng dụng, theo dõi phiên/kiểm toán và API quản trị.",
        "Xây dựng tích hợp: API service-to-service (tra cứu người dùng, thành viên ứng dụng) và đồng bộ "
        "Master Data giữa các hệ thống nội bộ.",
        "Quản lý chất lượng &amp; vận hành: kiểm thử xUnit trong CI, triển khai Docker trên dev / UAT / "
        "production, giám sát và backup; tự động hóa bằng Python + Gemini API.",
    ],

    "projects_en": [
        ("Multi-company financial &amp; fund reporting platform",
         "ABP / .NET · EF Core · SQL Server · Docker",
         ["MISA ledger import &amp; validation pipeline (44 companies), approval workflows and reporting "
          "APIs for the React SPA.",
          "EF Core migrations, multi-company data model and period management."]),
        ("Central SSO &amp; identity service",
         "ABP / .NET · OpenIddict / OIDC · SQL Server",
         ["OIDC flows (authorization-code + PKCE, client credentials), RBAC, per-application policies, "
          "session &amp; audit tracking.",
          "Service-to-service APIs: user lookup and application members for other systems."]),
        ("Construction project data platform",
         "ABP / .NET · EF Core · SQL Server · Docker",
         ["APIs for project coordination, member invitations and master-data synchronisation; released "
          "to production."]),
    ],
    "projects_vi": [
        ("Nền tảng báo cáo tài chính &amp; quỹ đa công ty",
         "ABP / .NET · EF Core · SQL Server · Docker",
         ["Pipeline nhập &amp; kiểm tra sổ MISA (44 công ty), quy trình duyệt và API báo cáo cho SPA React.",
          "Migration EF Core, mô hình dữ liệu đa công ty và quản lý kỳ báo cáo."]),
        ("Dịch vụ định danh &amp; SSO tập trung",
         "ABP / .NET · OpenIddict / OIDC · SQL Server",
         ["Luồng OIDC (authorization-code + PKCE, client credentials), RBAC, chính sách theo ứng dụng, "
          "theo dõi phiên &amp; kiểm toán.",
          "API service-to-service: tra cứu người dùng và thành viên ứng dụng cho hệ thống khác."]),
        ("Nền tảng dữ liệu dự án xây dựng",
         "ABP / .NET · EF Core · SQL Server · Docker",
         ["API cho điều phối dự án, mời thành viên và đồng bộ Master Data; đã phát hành production."]),
    ],
}
