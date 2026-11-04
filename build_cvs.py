#!/usr/bin/env python3
"""Sinh CV theo role cho Vũ Hữu Đô (HTML -> PDF).

- Nội dung nằm ở ROLES bên dưới (một nơi duy nhất).
- Mỗi role xuất ra roles/<id>/ gồm: bản EN (1 cột, thân thiện ATS) và bản VI (2 cột).
- Chạy:  python3 build_cvs.py     (cần Chromium; đặt CHROME=... nếu khác)

Lưu ý: chạy script sẽ GHI ĐÈ các file HTML/PDF trong roles/.
"""
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CHROME = os.environ.get("CHROME", "chromium")
AVATAR = os.path.join(ROOT, "html", "Avatar.png")

NAME_EN = "Vu Huu Do"
NAME_VI = "Vũ Hữu Đô"
CONTACT_LINE = (
    "Ho Chi Minh City, Vietnam &bull; +84 347 299 934 &bull; vuhuudo2004@gmail.com "
    "&bull; github.com/vuhuudo &bull; linkedin.com/in/vũ-hữu-đô-b899bb360"
)
JOB_EN = "Web &amp; Database Developer — Hoan Cau Group"
JOB_META_EN = "June 2025 – November 2026 · 1 yr 5 mos · Ho Chi Minh City, Vietnam"
JOB_VI = "Lập trình viên Web &amp; Cơ sở dữ liệu — Tập đoàn Hoàn Cầu"
JOB_META_VI = "06/2025 - 11/2026 (1 năm 5 tháng) · TP. Hồ Chí Minh"
EDUCATION_EN = ("<b>Bachelor of Artificial Intelligence</b> — Van Lang University, "
                "Ho Chi Minh City (2023 – 2026)")
EDUCATION_VI = ("<b>Cử nhân Trí tuệ nhân tạo</b> — Đại học Văn Lang (2023 - 2026)")
LANGUAGES_EN = "Vietnamese (native) · English (elementary)"
LANGUAGES_VI = "Tiếng Việt (bản ngữ) · Tiếng Anh (cơ bản)"

# ---------------------------------------------------------------- roles ----
ROLES = [
    {
        "id": "software-engineer",
        "file": "SoftwareEngineer",
        "title_en": "Software Engineer — Full Stack &amp; Platform",
        "title_vi": "Kỹ sư phần mềm — Full Stack &amp; Nền tảng",
        "badge_vi": "KỸ SƯ PHẦN MỀM",
        "summary_en": (
            "Software Engineer with 1.5 years of hands-on experience delivering and operating "
            "enterprise platforms at Hoan Cau Group. Works across the stack: C#/.NET (ABP Framework) "
            "APIs, React + TypeScript front-ends, SQL Server, and the Docker/Linux infrastructure with "
            "CI/CD and monitoring. Built a central OpenID Connect sign-on service for five internal "
            "applications and shipped multi-company reporting and project-data platforms to production. "
            "AI graduate; automates workflows with Python + Gemini API."
        ),
        "summary_vi": (
            "Kỹ sư phần mềm với 1,5 năm kinh nghiệm xây dựng và vận hành nền tảng nội bộ tại Tập đoàn "
            "Hoàn Cầu. Làm việc xuyên suốt stack: API C#/.NET (ABP Framework), giao diện React + "
            "TypeScript, SQL Server và hạ tầng Docker/Linux kèm CI/CD, giám sát. Đã xây dựng dịch vụ "
            "đăng nhập tập trung OpenID Connect cho 5 ứng dụng nội bộ; đưa nền tảng báo cáo đa công ty "
            "và nền tảng dữ liệu dự án lên production. Tốt nghiệp AI; tự động hóa bằng Python + Gemini API."
        ),
        "skills_en": [
            ("Languages:", "C#, TypeScript / JavaScript, Python, SQL (T-SQL), Bash"),
            ("Frameworks:", ".NET (ASP.NET Core), ABP Framework, React, Entity Framework Core, REST APIs, Vite"),
            ("Auth &amp; Data:", "OpenID Connect / OAuth2 (OpenIddict), RBAC, SQL Server, PostgreSQL, Pandas / NumPy"),
            ("Infrastructure:", "Docker, Docker Compose, Linux, WSL, Git / Gitea, CI/CD (Gitea Actions), Nginx, "
                               "Traefik / Pangolin, Prometheus &amp; Grafana, backup &amp; restore"),
            ("Practices:", "Automated testing (xUnit, Vitest, Playwright), code review, technical documentation, "
                           "rollback-safe releases"),
            ("AI &amp; Automation:", "Gemini API integration, Python automation, workflow optimisation"),
        ],
        "skills_vi": [
            ("Ngôn ngữ:", "C#, TypeScript / JavaScript, Python, SQL (T-SQL), Bash"),
            ("Framework:", ".NET (ASP.NET Core), ABP Framework, React, Entity Framework Core, REST API, Vite"),
            ("Xác thực &amp; Dữ liệu:", "OpenID Connect / OAuth2 (OpenIddict), RBAC, SQL Server, PostgreSQL, Pandas / NumPy"),
            ("Hạ tầng:", "Docker, Docker Compose, Linux, WSL, Git / Gitea, CI/CD (Gitea Actions), Nginx, "
                        "Traefik / Pangolin, Prometheus &amp; Grafana, backup &amp; restore"),
            ("Quy trình:", "Kiểm thử tự động (xUnit, Vitest, Playwright), review code, viết tài liệu, "
                          "phát hành có rollback"),
            ("AI &amp; Tự động hóa:", "Tích hợp Gemini API, tự động hóa bằng Python, tối ưu quy trình"),
        ],
        "exp_en": [
            "Delivered internal platforms end-to-end — .NET (ABP Framework) APIs, React + TypeScript UIs and "
            "SQL Server — including a <b>multi-company financial reporting platform</b> (44 companies: MISA "
            "ledger import &amp; validation, approval workflows, dashboards) and a <b>construction project "
            "data platform</b>, both in production.",
            "Built a central <b>OpenID Connect (OpenIddict)</b> sign-on service for <b>5 internal applications</b>: "
            "SPA flows with PKCE, client-credentials service scopes, role-based access, per-application catalogue "
            "&amp; policies, session/location tracking, audit logs and an admin console.",
            "Operate the full delivery pipeline across <b>three environments (dev / UAT / production)</b>: "
            "Docker &amp; Linux, CI/CD with Gitea Actions (build, automated test gates, security scans), "
            "reverse proxy (Traefik / Pangolin), Prometheus/Grafana alerting, scheduled backups and "
            "rollback-safe releases.",
            "Automate internal data workflows with Python (WSL) + Gemini API, removing repetitive manual "
            "processing for management teams.",
            "Led the Base.vn rollout at the <b>HCM head office and Khanh Hoa branch</b>; tracked project "
            "milestones and reported progress directly to the Board of Directors.",
        ],
        "exp_vi": [
            "Xây dựng nền tảng nội bộ trọn gói — API .NET (ABP Framework), giao diện React + TypeScript, "
            "SQL Server — gồm <b>nền tảng báo cáo tài chính đa công ty</b> (44 công ty: nhập &amp; kiểm tra "
            "sổ MISA, quy trình duyệt, dashboard) và <b>nền tảng dữ liệu dự án xây dựng</b>, cả hai đã lên production.",
            "Xây dựng dịch vụ đăng nhập tập trung <b>OpenID Connect (OpenIddict)</b> cho <b>5 ứng dụng nội bộ</b>: "
            "luồng SPA với PKCE, client-credentials cho service, phân quyền theo vai trò, danh mục &amp; chính sách "
            "theo ứng dụng, theo dõi phiên theo vùng, nhật ký kiểm toán và màn quản trị.",
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
             ["Period-based reporting for 44 companies: MISA ledger import &amp; validation, approval "
              "workflows, dashboards for accounting teams.",
              "Three-environment delivery with automated tests, health checks, monitoring and backup/restore."]),
            ("Central SSO &amp; identity service",
             "ABP / .NET · OpenIddict / OIDC · SQL Server · Docker",
             ["Single sign-on and application catalogue for 5 internal applications; admin console for users, "
              "roles, sessions and audit history.",
              "Service-to-service APIs (user lookup, application members) for access verification and sync."]),
            ("Construction project data platform",
             "ABP / .NET · React · TypeScript · Docker",
             ["Investor-side project data: coordination workspace, member invitations and master-data "
              "synchronisation; released to production."]),
        ],
        "projects_vi": [
            ("Nền tảng báo cáo tài chính &amp; quỹ đa công ty",
             "ABP / .NET · React · TypeScript · SQL Server · Docker",
             ["Báo cáo theo kỳ cho 44 công ty: nhập &amp; kiểm tra sổ MISA, quy trình duyệt, dashboard cho khối kế toán.",
              "Vận hành 3 môi trường với kiểm thử tự động, health check, giám sát và backup/restore."]),
            ("Dịch vụ định danh &amp; SSO tập trung",
             "ABP / .NET · OpenIddict / OIDC · SQL Server · Docker",
             ["SSO và danh mục ứng dụng cho 5 ứng dụng nội bộ; màn quản trị người dùng/vai trò/phiên/nhật ký.",
              "API dịch vụ (tra cứu người dùng, thành viên ứng dụng) để xác minh và đồng bộ quyền truy cập."]),
            ("Nền tảng dữ liệu dự án xây dựng",
             "ABP / .NET · React · TypeScript · Docker",
             ["Dữ liệu dự án phía chủ đầu tư: không gian điều phối, mời thành viên, đồng bộ Master Data; "
              "đã phát hành production."]),
        ],
    },
    {
        "id": "backend-dotnet",
        "file": "BackendDotNet",
        "title_en": "Backend Developer — .NET / C#",
        "title_vi": "Lập trình viên Backend — .NET / C#",
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
            "pipeline nhập &amp; kiểm tra dữ liệu nặng và quy trình duyệt đa công ty. Mạnh về xác thực &amp; phân "
            "quyền (OpenID Connect / OpenIddict, OAuth2 client credentials, RBAC) và tích hợp hệ thống; vận hành "
            "sản phẩm với Docker, CI/CD và giám sát."
        ),
        "skills_en": [
            ("Backend:", "C#, .NET (ASP.NET Core), ABP Framework, Entity Framework Core, REST APIs, "
                         "validation &amp; import pipelines"),
            ("Auth &amp; Security:", "OpenID Connect / OAuth2 (OpenIddict), authorization-code + PKCE, "
                                    "client credentials, RBAC, audit logging"),
            ("Data:", "SQL Server (T-SQL, schema design, EF Core migrations), PostgreSQL, "
                      "data validation, Python (Pandas, NumPy)"),
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
            ("Dữ liệu:", "SQL Server (T-SQL, thiết kế schema, EF Core migrations), PostgreSQL, "
                        "kiểm tra dữ liệu, Python (Pandas, NumPy)"),
            ("Tích hợp:", "API service-to-service, đồng bộ Master Data, webhook, API tra cứu người dùng"),
            ("Chất lượng &amp; Vận hành:", "xUnit, cổng kiểm thử &amp; quét bảo mật trong CI, Docker, Linux, "
                                          "Gitea Actions CI/CD, Prometheus / Grafana"),
            ("Bổ trợ:", "React + TypeScript, tự động hóa Python + Gemini API"),
        ],
        "exp_en": [
            "Designed and shipped .NET APIs for two production platforms: a <b>multi-company financial "
            "reporting platform</b> (44 companies — MISA ledger import &amp; validation, approval workflows) "
            "and a <b>construction project data platform</b> (coordination, member invitations, master-data sync).",
            "Built the domain, data and API layers: ABP Framework modules, EF Core + SQL Server schemas and "
            "migrations, REST endpoints consumed by React SPAs and other systems.",
            "Implemented authentication &amp; access control: central <b>OIDC / OpenIddict</b> service "
            "(authorization-code + PKCE, client-credentials service scopes), role-based access, per-application "
            "policies, session/audit tracking and admin APIs.",
            "Delivered integrations: service-to-service APIs (user lookup, application members) and "
            "master-data synchronisation between internal systems.",
            "Own quality &amp; operations: xUnit tests wired into CI, Dockerized deployments across "
            "dev / UAT / production, monitoring and backups; automate workflows with Python + Gemini API.",
        ],
        "exp_vi": [
            "Thiết kế và phát triển API .NET cho hai nền tảng production: <b>nền tảng báo cáo tài chính đa "
            "công ty</b> (44 công ty — nhập &amp; kiểm tra sổ MISA, quy trình duyệt) và <b>nền tảng dữ liệu dự án "
            "xây dựng</b> (điều phối, mời thành viên, đồng bộ Master Data).",
            "Xây dựng tầng domain, dữ liệu và API: module ABP Framework, schema &amp; migration EF Core + "
            "SQL Server, REST endpoint cho SPA React và các hệ thống khác.",
            "Triển khai xác thực &amp; phân quyền: dịch vụ <b>OIDC / OpenIddict</b> tập trung "
            "(authorization-code + PKCE, client-credentials cho service), phân quyền theo vai trò, chính sách "
            "theo ứng dụng, theo dõi phiên/kiểm toán và API quản trị.",
            "Xây dựng tích hợp: API service-to-service (tra cứu người dùng, thành viên ứng dụng) và đồng bộ "
            "Master Data giữa các hệ thống nội bộ.",
            "Quản lý chất lượng &amp; vận hành: kiểm thử xUnit trong CI, triển khai Docker trên "
            "dev / UAT / production, giám sát và backup; tự động hóa bằng Python + Gemini API.",
        ],
        "projects_en": [
            ("Multi-company financial &amp; fund reporting platform",
             "ABP / .NET · EF Core · SQL Server · Docker",
             ["MISA ledger import &amp; validation pipeline (44 companies), approval workflows and "
              "reporting APIs for the React SPA.",
              "EF Core migrations, multi-company data model and period management."]),
            ("Central SSO &amp; identity service",
             "ABP / .NET · OpenIddict / OIDC · SQL Server",
             ["OIDC flows (authorization-code + PKCE, client credentials), RBAC, per-application policies, "
              "session &amp; audit tracking.",
              "Service-to-service APIs: user lookup and application members for other systems."]),
            ("Construction project data platform",
             "ABP / .NET · EF Core · SQL Server · Docker",
             ["APIs for project coordination, member invitations and master-data synchronisation; "
              "released to production."]),
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
    },
    {
        "id": "frontend-react",
        "file": "FrontendReact",
        "title_en": "Frontend Developer — React / TypeScript",
        "title_vi": "Lập trình viên Frontend — React / TypeScript",
        "badge_vi": "LẬP TRÌNH VIÊN FRONTEND",
        "summary_en": (
            "Frontend-focused developer with 1.5 years building React + TypeScript applications at Hoan Cau "
            "Group. Ships data-dense internal UIs — dashboards, tables, multi-step import and approval flows — "
            "with clean component structure, vi/en internationalisation and automated test coverage. Integrates "
            "SPA authentication with OpenID Connect (authorization-code + PKCE) and works comfortably with the "
            ".NET APIs and SQL data behind the UI."
        ),
        "summary_vi": (
            "Lập trình viên thiên về frontend với 1,5 năm xây dựng ứng dụng React + TypeScript tại Tập đoàn "
            "Hoàn Cầu. Phát triển giao diện nội bộ dày dữ liệu — dashboard, bảng biểu, luồng nhập liệu &amp; "
            "duyệt nhiều bước — với cấu trúc component rõ ràng, đa ngôn ngữ vi/en và kiểm thử tự động. Tích hợp "
            "xác thực SPA với OpenID Connect (authorization-code + PKCE), làm việc tốt với API .NET và dữ liệu "
            "SQL phía sau."
        ),
        "skills_en": [
            ("Frontend:", "React, TypeScript, JavaScript, Vite, HTML5, CSS3, responsive web design, "
                          "component architecture"),
            ("UI patterns:", "Dashboards &amp; data tables, multi-step forms &amp; wizards, i18n (vi/en), "
                             "theming &amp; branding"),
            ("Auth:", "OIDC SPA integration (authorization-code + PKCE), token renewal, session-expiry UX"),
            ("Testing:", "Vitest (unit), Playwright (E2E), CI test gates"),
            ("Backend awareness:", "REST APIs, .NET / ABP, SQL Server"),
            ("Tooling:", "Git / Gitea, Gitea Actions, Docker"),
        ],
        "skills_vi": [
            ("Frontend:", "React, TypeScript, JavaScript, Vite, HTML5, CSS3, giao diện responsive, "
                          "kiến trúc component"),
            ("Mẫu UI:", "Dashboard &amp; bảng dữ liệu, form/wizard nhiều bước, đa ngôn ngữ (vi/en), "
                       "theme &amp; thương hiệu"),
            ("Xác thực:", "Tích hợp OIDC cho SPA (authorization-code + PKCE), gia hạn token, xử lý hết phiên"),
            ("Kiểm thử:", "Vitest (unit), Playwright (E2E), cổng kiểm thử trong CI"),
            ("Hiểu backend:", "REST API, .NET / ABP, SQL Server"),
            ("Công cụ:", "Git / Gitea, Gitea Actions, Docker"),
        ],
        "exp_en": [
            "Built the React + TypeScript UIs of two production platforms: a <b>multi-company financial "
            "reporting platform</b> (dashboards, period &amp; company navigation, MISA import and approval "
            "flows) and a <b>construction project data platform</b> (coordination workspace, member "
            "invitations, master-data screens).",
            "Integrated SPA authentication with the central <b>OIDC</b> service (authorization-code + PKCE, "
            "silent token renewal, session-expiry handling).",
            "Delivered UI quality at scale: responsive layouts, vi/en i18n, theming/branding, data-dense "
            "tables with sorting and filtering.",
            "Covered the UI with automated tests — Vitest unit tests and Playwright E2E — wired into CI "
            "alongside the .NET APIs.",
            "Worked full-cycle with .NET APIs and SQL-backed data; automate internal workflows with "
            "Python + Gemini API; led Base.vn rollout (HCM HQ, Khanh Hoa branch).",
        ],
        "exp_vi": [
            "Xây dựng giao diện React + TypeScript cho hai nền tảng production: <b>nền tảng báo cáo tài chính "
            "đa công ty</b> (dashboard, điều hướng theo kỳ/công ty, luồng nhập &amp; duyệt sổ MISA) và "
            "<b>nền tảng dữ liệu dự án xây dựng</b> (không gian điều phối, mời thành viên, màn Master Data).",
            "Tích hợp xác thực SPA với dịch vụ <b>OIDC</b> tập trung (authorization-code + PKCE, gia hạn token "
            "ngầm, xử lý hết phiên).",
            "Đảm bảo chất lượng giao diện: layout responsive, đa ngôn ngữ vi/en, theme/thương hiệu, bảng dữ "
            "liệu dày đặc với sắp xếp và lọc.",
            "Phủ kiểm thử tự động cho giao diện — Vitest (unit) và Playwright (E2E) — chạy trong CI cùng API .NET.",
            "Làm việc trọn vòng với API .NET và dữ liệu SQL; tự động hóa bằng Python + Gemini API; chủ trì "
            "triển khai Base.vn (hội sở HCM, chi nhánh Khánh Hòa).",
        ],
        "projects_en": [
            ("Multi-company financial &amp; fund reporting platform (React SPA)",
             "React · TypeScript · Vite · REST APIs",
             ["Dashboards and data-dense tables for 44 companies; period &amp; company navigation; "
              "MISA import and approval flows.",
              "vi/en internationalisation, theming and responsive layouts; Vitest + Playwright coverage."]),
            ("Central SSO — SPA integration",
             "OIDC (PKCE) · React · TypeScript",
             ["Authorization-code + PKCE flow, silent token renewal and session-expiry UX for internal SPAs."]),
            ("Construction project data platform (React UI)",
             "React · TypeScript · Vite",
             ["Coordination workspace, member invitations and master-data screens; released to production."]),
        ],
        "projects_vi": [
            ("Nền tảng báo cáo tài chính đa công ty (SPA React)",
             "React · TypeScript · Vite · REST API",
             ["Dashboard và bảng dữ liệu dày đặc cho 44 công ty; điều hướng theo kỳ &amp; công ty; "
              "luồng nhập và duyệt sổ MISA.",
              "Đa ngôn ngữ vi/en, theme và layout responsive; kiểm thử Vitest + Playwright."]),
            ("SSO tập trung — tích hợp SPA",
             "OIDC (PKCE) · React · TypeScript",
             ["Luồng authorization-code + PKCE, gia hạn token ngầm và xử lý hết phiên cho các SPA nội bộ."]),
            ("Nền tảng dữ liệu dự án xây dựng (giao diện React)",
             "React · TypeScript · Vite",
             ["Không gian điều phối, mời thành viên và màn Master Data; đã phát hành production."]),
        ],
    },
    {
        "id": "devops",
        "file": "DevOps",
        "title_en": "DevOps Engineer — Docker / Linux / CI-CD",
        "title_vi": "Kỹ sư DevOps — Docker / Linux / CI-CD",
        "badge_vi": "KỸ SƯ DEVOPS",
        "summary_en": (
            "DevOps-minded engineer with 1.5 years building and running internal platforms at Hoan Cau Group. "
            "Operates multiple systems across three environments (dev / UAT / production) on Docker &amp; Linux: "
            "CI/CD with Gitea Actions, reverse proxy &amp; TLS, monitoring &amp; alerting (Prometheus / Grafana), "
            "scheduled backups and rollback-safe releases. Also develops on the stack (.NET / React), so tooling "
            "and pipelines fit the teams' real needs."
        ),
        "summary_vi": (
            "Kỹ sư thiên về DevOps với 1,5 năm xây dựng và vận hành nền tảng nội bộ tại Tập đoàn Hoàn Cầu. "
            "Vận hành nhiều hệ thống trên 3 môi trường (dev / UAT / production) với Docker &amp; Linux: CI/CD "
            "Gitea Actions, reverse proxy &amp; TLS, giám sát &amp; cảnh báo (Prometheus / Grafana), backup định "
            "kỳ và phát hành có rollback. Đồng thời phát triển trên chính stack đó (.NET / React) nên pipeline "
            "và công cụ sát nhu cầu thực tế của đội."
        ),
        "skills_en": [
            ("Containers &amp; OS:", "Docker, Docker Compose, Linux (Ubuntu), WSL, Bash"),
            ("CI/CD:", "Gitea (self-hosted Git), Gitea Actions pipelines, automated test gates, security scans, "
                       "versioned releases &amp; rollback"),
            ("Networking &amp; edge:", "Nginx, Traefik, Pangolin (reverse proxy / remote access), DNS &amp; TLS, "
                                       "WireGuard (wg-easy) VPN"),
            ("Observability:", "Prometheus, Grafana, Alertmanager, node-exporter; health checks &amp; alert design"),
            ("Data operations:", "SQL Server on Docker, scheduled backups &amp; restore drills, "
                                 "capacity &amp; cleanup automation"),
            ("Development:", "C# / .NET, React + TypeScript, Python + Gemini API automation"),
        ],
        "skills_vi": [
            ("Container &amp; OS:", "Docker, Docker Compose, Linux (Ubuntu), WSL, Bash"),
            ("CI/CD:", "Gitea (Git tự vận hành), pipeline Gitea Actions, cổng kiểm thử tự động, quét bảo mật, "
                      "phát hành theo version &amp; rollback"),
            ("Mạng &amp; edge:", "Nginx, Traefik, Pangolin (reverse proxy / truy cập từ xa), DNS &amp; TLS, "
                                "VPN WireGuard (wg-easy)"),
            ("Giám sát:", "Prometheus, Grafana, Alertmanager, node-exporter; health check &amp; thiết kế cảnh báo"),
            ("Vận hành dữ liệu:", "SQL Server trên Docker, backup định kỳ &amp; diễn tập restore, "
                                  "tự động hóa dọn dung lượng"),
            ("Phát triển:", "C# / .NET, React + TypeScript, tự động hóa Python + Gemini API"),
        ],
        "exp_en": [
            "Built and operate the delivery platform for multiple internal systems across <b>three environments "
            "(dev / UAT / production)</b>: Dockerized services, self-hosted registry, CI/CD pipelines in Gitea "
            "Actions (build → test gates → security scan → deploy) with rollback-safe releases.",
            "Run the edge &amp; access layer: reverse proxy (Traefik / Pangolin) with per-application routing "
            "and TLS; SSO-protected internal tools; WireGuard VPN access for branches (region mapping).",
            "Set up observability &amp; reliability: Prometheus + Grafana dashboards and alerts (service health, "
            "data blobs, backups, disk), health checks, scheduled backups with restore drills, incident "
            "handling and capacity cleanup.",
            "Operate SQL Server on Docker for several systems: backup/restore, migration runs and monitoring "
            "of long-running import jobs.",
            "Also develop on the stack (.NET / React) and automate workflows with Python + Gemini API; led the "
            "Base.vn rollout at HCM head office and Khanh Hoa branch.",
        ],
        "exp_vi": [
            "Xây dựng và vận hành nền tảng phát hành cho nhiều hệ thống nội bộ trên <b>3 môi trường "
            "(dev / UAT / production)</b>: dịch vụ đóng gói Docker, registry tự vận hành, pipeline CI/CD "
            "trong Gitea Actions (build → kiểm thử → quét bảo mật → deploy) với phát hành có rollback.",
            "Vận hành tầng edge &amp; truy cập: reverse proxy (Traefik / Pangolin) định tuyến theo ứng dụng "
            "và TLS; công cụ nội bộ bảo vệ bằng SSO; VPN WireGuard cho chi nhánh (ánh xạ theo vùng).",
            "Thiết lập giám sát &amp; độ tin cậy: dashboard và cảnh báo Prometheus + Grafana (sức khỏe dịch vụ, "
            "file dữ liệu, backup, dung lượng), health check, backup định kỳ kèm diễn tập restore, xử lý sự cố "
            "và dọn dung lượng.",
            "Vận hành SQL Server trên Docker cho nhiều hệ thống: backup/restore, chạy migration và theo dõi "
            "các job nhập dữ liệu dài.",
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
              "Scheduled SQL Server backups with restore drills; WireGuard VPN (wg-easy) for branch access "
              "with region mapping."]),
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
              "Backup SQL Server định kỳ kèm diễn tập restore; VPN WireGuard (wg-easy) cho chi nhánh, "
              "ánh xạ theo vùng."]),
            ("Công cụ tự động hóa &amp; bảo trì",
             "Python · Bash · WSL",
             ["Job dọn dẹp &amp; bảo trì định kỳ; tự động hóa quy trình nội bộ bằng Python + Gemini API."]),
        ],
    },
    {
        "id": "ai-automation",
        "file": "AIAutomation",
        "title_en": "AI &amp; Automation Engineer — Python / LLM APIs",
        "title_vi": "Kỹ sư AI &amp; Tự động hóa — Python / LLM API",
        "badge_vi": "KỸ SƯ AI &amp; TỰ ĐỘNG HÓA",
        "summary_en": (
            "AI graduate (Van Lang University) and hands-on automation engineer with 1.5 years at Hoan Cau "
            "Group. Builds Python workflows that combine LLM APIs (Gemini) with data processing to automate "
            "internal operations — and ships the surrounding software (.NET / React) and infrastructure "
            "(Docker, CI/CD, monitoring). Strong at turning messy manual processes into reliable, monitored "
            "pipelines."
        ),
        "summary_vi": (
            "Tốt nghiệp ngành Trí tuệ nhân tạo (Đại học Văn Lang), kỹ sư tự động hóa với 1,5 năm tại Tập đoàn "
            "Hoàn Cầu. Xây dựng quy trình Python kết hợp LLM API (Gemini) với xử lý dữ liệu để tự động hóa "
            "vận hành nội bộ — đồng thời phát triển phần mềm xung quanh (.NET / React) và hạ tầng (Docker, "
            "CI/CD, giám sát). Mạnh về biến quy trình thủ công phức tạp thành pipeline ổn định, có giám sát."
        ),
        "skills_en": [
            ("AI &amp; LLM:", "Gemini API integration, prompt &amp; workflow design, automation pipelines; "
                             "AI/ML fundamentals (B.Sc. Artificial Intelligence)"),
            ("Python:", "Automation scripts, data processing (Pandas, NumPy), REST API integration, WSL"),
            ("Data:", "SQL (T-SQL / PostgreSQL), Excel / MISA data handling, validation pipelines"),
            ("Software:", "C# / .NET (ABP Framework), React + TypeScript, REST APIs"),
            ("Operations:", "Docker, Linux / WSL, CI/CD (Gitea Actions), Prometheus / Grafana monitoring, backups"),
        ],
        "skills_vi": [
            ("AI &amp; LLM:", "Tích hợp Gemini API, thiết kế prompt &amp; workflow, pipeline tự động hóa; "
                             "nền tảng AI/ML (Cử nhân Trí tuệ nhân tạo)"),
            ("Python:", "Script tự động hóa, xử lý dữ liệu (Pandas, NumPy), tích hợp REST API, WSL"),
            ("Dữ liệu:", "SQL (T-SQL / PostgreSQL), xử lý dữ liệu Excel / MISA, pipeline kiểm tra dữ liệu"),
            ("Phần mềm:", "C# / .NET (ABP Framework), React + TypeScript, REST API"),
            ("Vận hành:", "Docker, Linux / WSL, CI/CD (Gitea Actions), giám sát Prometheus / Grafana, backup"),
        ],
        "exp_en": [
            "Built Python (WSL) + <b>Gemini API</b> automation pipelines for internal data extraction and "
            "processing, removing repetitive manual work for management teams.",
            "Automated executive milestone tracking: summarised project progress and produced reporting "
            "inputs used directly with the Board of Directors.",
            "Led the <b>Base.vn</b> digital-transformation rollout at the HCM head office and Khanh Hoa branch, "
            "standardising workflows and communication.",
            "Engineered the data pipeline of a multi-company reporting platform: MISA ledger import, parsing "
            "and validation across <b>44 companies</b>.",
            "Delivered the surrounding software end-to-end: .NET APIs, React UIs, a central SSO service, and "
            "Docker / CI-CD infrastructure with monitoring and backups.",
        ],
        "exp_vi": [
            "Xây dựng pipeline tự động hóa Python (WSL) + <b>Gemini API</b> để trích xuất và xử lý dữ liệu "
            "nội bộ, loại bỏ việc thủ công lặp lại cho bộ phận quản lý.",
            "Tự động hóa theo dõi mốc tiến độ: tổng hợp tiến độ dự án và tạo đầu vào báo cáo dùng trực tiếp "
            "với Ban Tổng Giám đốc.",
            "Chủ trì triển khai chuyển đổi số <b>Base.vn</b> tại hội sở HCM và chi nhánh Khánh Hòa, chuẩn hóa "
            "quy trình và truyền thông nội bộ.",
            "Xây dựng pipeline dữ liệu của nền tảng báo cáo đa công ty: nhập, phân tích và kiểm tra sổ MISA "
            "cho <b>44 công ty</b>.",
            "Phát triển trọn gói phần mềm xung quanh: API .NET, giao diện React, dịch vụ SSO tập trung và hạ "
            "tầng Docker / CI-CD kèm giám sát, backup.",
        ],
        "projects_en": [
            ("LLM automation pipelines",
             "Python · Gemini API · WSL",
             ["Automated internal data extraction and processing workflows that replace repetitive manual "
              "steps for management teams.",
              "Runs on Linux/WSL alongside the group's internal platforms, with logging for follow-up."]),
            ("Reporting data pipeline (MISA import)",
             ".NET · SQL Server · Excel / MISA data",
             ["Ledger import, parsing and validation pipeline covering 44 companies with per-row error "
              "reporting."]),
            ("Platform engineering (context)",
             ".NET · React · Docker · CI/CD",
             ["Central OIDC SSO for 5 internal applications; reporting and project-data platforms shipped "
              "to production."]),
        ],
        "projects_vi": [
            ("Pipeline tự động hóa với LLM",
             "Python · Gemini API · WSL",
             ["Tự động hóa trích xuất &amp; xử lý dữ liệu nội bộ, thay thế các bước thủ công lặp lại cho "
              "bộ phận quản lý.",
              "Chạy trên Linux/WSL song song với các nền tảng nội bộ, có ghi log để theo dõi."]),
            ("Pipeline dữ liệu báo cáo (nhập sổ MISA)",
             ".NET · SQL Server · dữ liệu Excel / MISA",
             ["Pipeline nhập, phân tích và kiểm tra sổ cho 44 công ty, báo lỗi theo từng dòng."]),
            ("Kỹ thuật nền tảng (bối cảnh)",
             ".NET · React · Docker · CI/CD",
             ["SSO OIDC tập trung cho 5 ứng dụng nội bộ; nền tảng báo cáo và dữ liệu dự án đã lên production."]),
        ],
    },
]

# ------------------------------------------------------------- templates ---
CONTACT_SVGS = {
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>',
}
CONTACT_VI = [
    ("pin", "TP. Hồ Chí Minh, Việt Nam"),
    ("phone", "+84 347 299 934"),
    ("mail", '<a href="mailto:vuhuudo2004@gmail.com">vuhuudo2004@gmail.com</a>'),
    ("github", '<a href="https://github.com/vuhuudo">github.com/vuhuudo</a>'),
    ("linkedin", '<a href="https://www.linkedin.com/in/v%C5%A9-h%E1%BB%AFu-%C4%91%C3%B4-b899bb360/">linkedin.com/in/vũ-hữu-đô-b899bb360</a>'),
]

ATS_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{{NAME}} — {{TITLE}} — CV</title>
<style>
  :root { --ink:#161616; --accent:#0b5394; --muted:#4a4a4a; }
  * { box-sizing: border-box; }
  body { font-family: Calibri, Carlito, 'Segoe UI', Arial, sans-serif; color: var(--ink);
         font-size: 9.9pt; line-height: 1.26; margin: 0; padding: 0; }
  .page { max-width: 820px; margin: 0 auto; padding: 22px 26px; }
  header { text-align: center; margin-bottom: 6px; }
  h1 { font-size: 19pt; letter-spacing: .6px; margin: 0 0 2px; text-transform: uppercase; }
  .title { font-size: 10.8pt; font-weight: 700; color: var(--accent); margin-bottom: 4px; }
  .contact { font-size: 9.4pt; color: var(--muted); }
  h2 { font-size: 10.8pt; text-transform: uppercase; letter-spacing: .7px; color: var(--accent);
       border-bottom: 1.5px solid var(--accent); padding-bottom: 2px; margin: 7px 0 4px; }
  p { margin: 2px 0; }
  ul { margin: 2px 0 0; padding-left: 16px; }
  li { margin-bottom: 1.2px; }
  .role { font-weight: 700; font-size: 10.7pt; margin: 0; }
  .meta { font-style: italic; color: var(--muted); font-size: 9.3pt; margin: 1px 0 2px; }
  .proj { margin-top: 4px; }
  .proj .name { font-weight: 700; margin: 0; }
  .proj .tech { color: var(--muted); font-size: 9.2pt; font-style: italic; margin: 0 0 1px; }
  .skills p { margin: 1.5px 0; }
  @media print { @page { size: A4 portrait; margin: 10mm 11mm; } .page { padding: 0; max-width: none; } }
</style>
</head>
<body>
<div class="page">
  <header>
    <h1>{{NAME}}</h1>
    <div class="title">{{TITLE}}</div>
    <div class="contact">{{CONTACT}}</div>
  </header>
  <h2>Summary</h2>
  <p>{{SUMMARY}}</p>
  <h2>Core Skills</h2>
  <div class="skills">{{SKILLS}}</div>
  <h2>Professional Experience</h2>
  <div>
    <p class="role">{{JOB}}</p>
    <p class="meta">{{JOB_META}}</p>
    <ul>{{BULLETS}}</ul>
  </div>
  <h2>Selected Projects</h2>
  {{PROJECTS}}
  <h2>Education &amp; Languages</h2>
  <p>{{EDUCATION}} &nbsp;·&nbsp; {{LANGUAGES}}</p>
</div>
</body>
</html>
"""

VISUAL_HTML = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<title>{{NAME}} - {{TITLE}} - CV</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', Calibri, Tahoma, Geneva, Verdana, sans-serif;
         background-color: #f5f5f5; color: #333; line-height: 1.36; padding: 20px; }
  .resume-container { max-width: 900px; margin: 0 auto; background: #fff; display: flex;
                      box-shadow: 0 0 15px rgba(0,0,0,0.1); }
  .sidebar { width: 31%; background-color: #f4f6f8; padding: 18px 15px; border-right: 1px solid #e1e4e8; }
  .profile-img-container { text-align: center; margin-bottom: 10px; }
  .profile-img { width: 100px; height: 100px; border-radius: 50%; object-fit: cover;
                 border: 3px solid #005080; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
  .name-title-container { text-align: center; margin-bottom: 12px; }
  .name-title-container h1 { font-size: 18.5px; font-weight: 700; color: #111827; text-transform: uppercase;
                             letter-spacing: .5px; line-height: 1.2; margin-bottom: 5px; }
  .name-title-container .job-badge { font-size: 10.5px; font-weight: 600; color: #005080;
      text-transform: uppercase; letter-spacing: .7px; border-top: 2px solid #005080;
      border-bottom: 2px solid #005080; padding: 3px 0; display: inline-block; width: 100%; }
  .sidebar-section { margin-bottom: 12px; }
  .sidebar-section h2 { font-size: 12.2px; font-weight: 700; color: #1e293b; text-transform: uppercase;
      border-bottom: 1.5px solid #1e293b; padding-bottom: 3px; margin-bottom: 6px; letter-spacing: .5px; }
  .contact-list { list-style: none; font-size: 10.2px; }
  .contact-list li { margin-bottom: 5px; display: flex; align-items: flex-start; word-break: break-word; }
  .contact-list svg { width: 13px; height: 13px; flex: 0 0 13px; color: #005080; margin-right: 6px; margin-top: 2px; }
  .contact-list a { color: #005080; text-decoration: none; }
  .sidebar-text { font-size: 10.2px; color: #4b5563; text-align: left; }
  .education-item { font-size: 10.2px; margin-bottom: 4px; }
  .education-item strong { color: #111827; display: block; }
  .education-item i { color: #6b7280; }
  .lang-list { list-style: none; font-size: 10.2px; }
  .lang-list li { margin-bottom: 3px; color: #374151; }
  .main-content { width: 69%; padding: 18px 20px; }
  .main-section { margin-bottom: 11px; }
  .main-section h2 { font-size: 13.2px; font-weight: 700; color: #1e293b; text-transform: uppercase;
      border-bottom: 2px solid #1e293b; padding-bottom: 3px; margin-bottom: 7px; letter-spacing: .5px; }
  .experience-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 1px; }
  .experience-title { font-size: 12px; font-weight: 700; color: #111827; }
  .company-name { font-size: 11.2px; font-weight: 700; color: #1e293b; text-transform: uppercase; }
  .job-date { font-size: 10.3px; font-style: italic; color: #6b7280; margin-bottom: 4px; }
  ul.bullet-list { padding-left: 16px; margin-bottom: 7px; font-size: 10.6px; }
  ul.bullet-list li { margin-bottom: 2.5px; color: #374151; text-align: left; }
  .project-block { margin-bottom: 7px; }
  .project-title { font-size: 12px; font-weight: 700; color: #111827; }
  .project-tech { font-size: 10.1px; font-style: italic; color: #6b7280; margin-bottom: 2px; }
  .skills-grid { display: flex; flex-direction: column; gap: 4px; }
  .skill-row { display: flex; font-size: 10.6px; }
  .skill-category { width: 27%; font-weight: 700; color: #111827; }
  .skill-details { width: 73%; color: #374151; }
  @media print {
    body { background: #fff; padding: 0; }
    .resume-container { box-shadow: none; max-width: 100%; width: 100%; }
    @page { margin: 0; size: A4 portrait; }
  }
</style>
</head>
<body>
<div class="resume-container">
  <div class="sidebar">
    <div class="profile-img-container">
      <img src="Avatar.png" alt="{{NAME}}" class="profile-img">
    </div>
    <div class="name-title-container">
      <h1>{{NAME}}</h1>
      <div class="job-badge">{{BADGE}}</div>
    </div>
    <div class="sidebar-section">
      <h2>LIÊN HỆ</h2>
      <ul class="contact-list">{{CONTACTS}}</ul>
    </div>
    <div class="sidebar-section">
      <h2>TÓM TẮT</h2>
      <p class="sidebar-text">{{SUMMARY}}</p>
    </div>
    <div class="sidebar-section">
      <h2>HỌC VẤN</h2>
      <div class="education-item">{{EDUCATION}}</div>
    </div>
    <div class="sidebar-section">
      <h2>NGÔN NGỮ</h2>
      <ul class="lang-list">{{LANGUAGES}}</ul>
    </div>
  </div>
  <div class="main-content">
    <div class="main-section">
      <h2>KINH NGHIỆM LÀM VIỆC</h2>
      <div>
        <div class="experience-header">
          <span class="experience-title">Lập trình viên Web &amp; Cơ sở dữ liệu</span>
          <span class="company-name">TẬP ĐOÀN HOÀN CẦU</span>
        </div>
        <div class="job-date">{{JOB_META}}</div>
        <ul class="bullet-list">{{BULLETS}}</ul>
      </div>
    </div>
    <div class="main-section">
      <h2>DỰ ÁN TIÊU BIỂU</h2>
      {{PROJECTS}}
    </div>
    <div class="main-section">
      <h2>KỸ NĂNG CHUYÊN MÔN</h2>
      <div class="skills-grid">{{SKILLS}}</div>
    </div>
  </div>
</div>
</body>
</html>
"""


def render_skills_ats(items):
    return "\n".join(f"    <p><b>{k}</b> {v}</p>" for k, v in items)


def render_skills_visual(items):
    return "\n".join(
        f'        <div class="skill-row"><div class="skill-category">{k}</div>'
        f'<div class="skill-details">{v}</div></div>'
        for k, v in items
    )


def render_bullets(items):
    return "\n".join(f"      <li>{b}</li>" for b in items)


def render_projects_ats(projects):
    blocks = []
    for name, tech, bullets in projects:
        bl = "\n".join(f"      <li>{b}</li>" for b in bullets)
        blocks.append(
            f'  <div class="proj">\n    <p class="name">{name}</p>\n'
            f'    <p class="tech">{tech}</p>\n    <ul>\n{bl}\n    </ul>\n  </div>'
        )
    return "\n".join(blocks)


def render_projects_visual(projects):
    blocks = []
    for name, tech, bullets in projects:
        bl = "\n".join(f"        <li>{b}</li>" for b in bullets)
        blocks.append(
            f'      <div class="project-block">\n        <div class="project-title">{name}</div>\n'
            f'        <div class="project-tech">{tech}</div>\n        <ul class="bullet-list">\n{bl}\n        </ul>\n      </div>'
        )
    return "\n".join(blocks)


def render_contacts_visual():
    out = []
    for kind, text in CONTACT_VI:
        out.append(f"        <li>{CONTACT_SVGS[kind]}<span>{text}</span></li>")
    return "\n".join(out)


def build_html(role, lang):
    if lang == "EN":
        html = ATS_HTML
        repl = {
            "{{NAME}}": NAME_EN,
            "{{TITLE}}": role["title_en"],
            "{{CONTACT}}": CONTACT_LINE,
            "{{SUMMARY}}": role["summary_en"],
            "{{SKILLS}}": render_skills_ats(role["skills_en"]),
            "{{JOB}}": JOB_EN,
            "{{JOB_META}}": JOB_META_EN,
            "{{BULLETS}}": render_bullets(role["exp_en"]),
            "{{PROJECTS}}": render_projects_ats(role["projects_en"]),
            "{{EDUCATION}}": EDUCATION_EN,
            "{{LANGUAGES}}": LANGUAGES_EN,
        }
    else:
        html = VISUAL_HTML
        repl = {
            "{{NAME}}": NAME_VI,
            "{{TITLE}}": role["title_vi"],
            "{{BADGE}}": role["badge_vi"],
            "{{CONTACTS}}": render_contacts_visual(),
            "{{SUMMARY}}": role["summary_vi"],
            "{{SKILLS}}": render_skills_visual(role["skills_vi"]),
            "{{JOB_META}}": JOB_META_VI,
            "{{BULLETS}}": render_bullets(role["exp_vi"]),
            "{{PROJECTS}}": render_projects_visual(role["projects_vi"]),
            "{{EDUCATION}}": EDUCATION_VI,
            "{{LANGUAGES}}": (
                "<li><strong>Tiếng Việt:</strong> Bản ngữ</li>"
                "<li><strong>Tiếng Anh:</strong> Cơ bản</li>"
            ),
        }
    for key, value in repl.items():
        html = html.replace(key, value)
    return html


def build_pdf(html_path, pdf_path):
    subprocess.run(
        [CHROME, "--headless", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", f"file://{html_path}"],
        check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    pages = "?"
    try:
        info = subprocess.run(["pdfinfo", pdf_path], capture_output=True, text=True).stdout
        for line in info.splitlines():
            if line.startswith("Pages:"):
                pages = line.split(":")[1].strip()
    except FileNotFoundError:
        pass
    return pages


def main():
    out_root = os.path.join(ROOT, "roles")
    warn = []
    for role in ROLES:
        folder = os.path.join(out_root, role["id"])
        os.makedirs(folder, exist_ok=True)
        shutil.copy(AVATAR, os.path.join(folder, "Avatar.png"))
        for lang in ("EN", "VI"):
            base = f"CV_VuHuuDo_{role['file']}_{lang}"
            html_path = os.path.join(folder, base + ".html")
            pdf_path = os.path.join(folder, base + ".pdf")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(build_html(role, lang))
            pages = build_pdf(html_path, pdf_path)
            status = "OK" if pages == "1" else f"⚠ {pages} trang"
            if pages != "1":
                warn.append(base)
            print(f"  {role['id']:<18} {lang}  ->  {base}.pdf  [{status}]")
    if warn:
        print("\nCẢNH BÁO: các bản sau chưa vừa 1 trang:", ", ".join(warn))
        sys.exit(1)


if __name__ == "__main__":
    main()
