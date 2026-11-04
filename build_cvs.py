#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Sinh CV theo role cho Vũ Hữu Đô (HTML -> PDF).

- Nội dung nằm ở ROLES bên dưới (một nơi duy nhất).
- Mỗi role xuất ra roles/<id>/ gồm: bản EN (1 cột, thân thiện ATS) và bản VI (2 cột).
- Chạy:  uv run build_cvs.py     (cần Chromium/Chrome; đặt CHROME=... nếu khác)

Lưu ý: chạy script sẽ GHI ĐÈ các file HTML/PDF trong roles/.
"""
import glob
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for n in ("chromium", "chromium-browser", "google-chrome", "chrome"):
        if shutil.which(n):
            return n
    hits = sorted(glob.glob(os.path.expanduser("~/.cache/ms-playwright/chromium-*/chrome-linux*/chrome")))
    return hits[-1] if hits else "chromium"


CHROME = find_chrome()
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
            "Software Engineer with 1.5 years of experience building and operating enterprise web "
            "platforms. Full-stack across C#/.NET (ABP Framework), React + TypeScript, SQL Server and "
            "Docker/Linux with CI/CD. Delivered reporting, authentication (OpenID Connect) and data "
            "platforms to production. AI graduate; automates workflows with Python."
        ),
        "summary_vi": (
            "Kỹ sư phần mềm với 1,5 năm kinh nghiệm xây dựng và vận hành nền tảng web doanh nghiệp. "
            "Full-stack với C#/.NET (ABP Framework), React + TypeScript, SQL Server và Docker/Linux kèm "
            "CI/CD. Đã đưa nền tảng báo cáo, xác thực (OpenID Connect) và dữ liệu lên production. "
            "Tốt nghiệp AI; tự động hóa quy trình bằng Python."
        ),
        "skills_en": [
            ("Languages:", "C#, TypeScript / JavaScript, Python, Rust, SQL, Bash"),
            ("Frameworks:", ".NET (ASP.NET Core), ABP Framework, React, Svelte, Entity Framework Core, REST APIs"),
            ("Auth &amp; Data:", "OpenID Connect / OAuth2, RBAC, SQL Server, PostgreSQL, ClickHouse"),
            ("DevOps:", "Docker, Linux, Git, CI/CD, reverse proxy, monitoring &amp; alerting, backup / restore"),
            ("Quality:", "Automated testing (xUnit, Vitest, Playwright), code review, documentation"),
            ("AI &amp; Automation:", "Python automation, LLM API integration"),
        ],
        "skills_vi": [
            ("Ngôn ngữ:", "C#, TypeScript / JavaScript, Python, Rust, SQL, Bash"),
            ("Framework:", ".NET (ASP.NET Core), ABP Framework, React, Svelte, Entity Framework Core, REST API"),
            ("Xác thực &amp; Dữ liệu:", "OpenID Connect / OAuth2, RBAC, SQL Server, PostgreSQL, ClickHouse"),
            ("DevOps:", "Docker, Linux, Git, CI/CD, reverse proxy, giám sát &amp; cảnh báo, backup / restore"),
            ("Chất lượng:", "Kiểm thử tự động (xUnit, Vitest, Playwright), review code, viết tài liệu"),
            ("AI &amp; Tự động hóa:", "Tự động hóa bằng Python, tích hợp LLM API"),
        ],
        "exp_en": [
            "Built internal platforms end-to-end: .NET (ABP) APIs, React + TypeScript UIs and SQL Server, "
            "including an enterprise reporting platform and a project-data platform, both in production.",
            "Implemented central single sign-on (OpenID Connect / OAuth2): PKCE flows, service-to-service "
            "access, role-based permissions, session management and audit logging.",
            "Built a data lakehouse (ClickHouse, PostgreSQL, S3) with a Python API, Svelte UI and a Rust core "
            "for file parsing and export; sharded CI cut test time by ~65%.",
            "Operated dev / UAT / production on Docker &amp; Linux: CI/CD with test gates, monitoring, "
            "alerting, backups and rollback-safe releases.",
        ],
        "exp_vi": [
            "Xây dựng nền tảng nội bộ trọn gói: API .NET (ABP), giao diện React + TypeScript, SQL Server, "
            "gồm nền tảng báo cáo doanh nghiệp và nền tảng dữ liệu dự án, đều đã lên production.",
            "Triển khai đăng nhập tập trung (OpenID Connect / OAuth2): luồng PKCE, truy cập giữa các dịch vụ, "
            "phân quyền theo vai trò, quản lý phiên và nhật ký kiểm toán.",
            "Xây dựng data lakehouse (ClickHouse, PostgreSQL, S3) với API Python, giao diện Svelte và lõi Rust "
            "xử lý/xuất tệp; CI chia shard giảm ~65% thời gian test.",
            "Vận hành dev / UAT / production trên Docker &amp; Linux: CI/CD có cổng kiểm thử, giám sát, "
            "cảnh báo, backup và phát hành có rollback.",
        ],
        "projects_en": [
            ("Enterprise reporting platform", "ABP / .NET · React · TypeScript · SQL Server · Docker",
             ["Multi-entity period reporting: data import &amp; validation, approval workflow, dashboards."]),
            ("Central authentication (SSO) service", "ABP / .NET · OpenID Connect · OAuth2 · SQL Server",
             ["Single sign-on, RBAC, session and audit management for internal applications."]),
            ("Data lakehouse &amp; analytics", "Python · Rust · ClickHouse · PostgreSQL · Svelte",
             ["Medallion-style pipeline with REST APIs, dashboards and automated tests."]),
        ],
        "projects_vi": [
            ("Nền tảng báo cáo doanh nghiệp", "ABP / .NET · React · TypeScript · SQL Server · Docker",
             ["Báo cáo theo kỳ đa đơn vị: nhập &amp; kiểm tra dữ liệu, quy trình duyệt, dashboard."]),
            ("Dịch vụ xác thực tập trung (SSO)", "ABP / .NET · OpenID Connect · OAuth2 · SQL Server",
             ["Đăng nhập một lần, RBAC, quản lý phiên và nhật ký kiểm toán cho các ứng dụng nội bộ."]),
            ("Data lakehouse &amp; phân tích", "Python · Rust · ClickHouse · PostgreSQL · Svelte",
             ["Pipeline kiểu Medallion với REST API, dashboard và kiểm thử tự động."]),
        ],
    },
    {
        "id": "backend-dotnet",
        "file": "BackendDotNet",
        "title_en": "Backend Developer — .NET / C#",
        "title_vi": "Lập trình viên Backend — .NET / C#",
        "badge_vi": "LẬP TRÌNH VIÊN BACKEND",
        "summary_en": (
            "Backend developer with 1.5 years building .NET services. Designs APIs with ABP Framework / "
            "ASP.NET Core, EF Core and SQL Server, including data import &amp; validation pipelines and "
            "approval workflows. Strong in authentication &amp; authorization (OpenID Connect, OAuth2, RBAC) "
            "and system integrations."
        ),
        "summary_vi": (
            "Lập trình viên backend với 1,5 năm xây dựng dịch vụ .NET. Thiết kế API với ABP Framework / "
            "ASP.NET Core, EF Core và SQL Server, gồm pipeline nhập &amp; kiểm tra dữ liệu và quy trình duyệt. "
            "Mạnh về xác thực &amp; phân quyền (OpenID Connect, OAuth2, RBAC) và tích hợp hệ thống."
        ),
        "skills_en": [
            ("Backend:", "C#, .NET (ASP.NET Core), ABP Framework, Entity Framework Core, REST APIs"),
            ("Auth &amp; Security:", "OpenID Connect / OAuth2, PKCE, client credentials, RBAC, audit logging"),
            ("Data:", "SQL Server (T-SQL, migrations), PostgreSQL, ClickHouse, data validation"),
            ("Integration:", "Service-to-service APIs, data synchronisation, webhooks"),
            ("Quality &amp; Ops:", "xUnit, CI test gates, Docker, Linux, monitoring"),
            ("Secondary:", "React + TypeScript, Python, Rust"),
        ],
        "skills_vi": [
            ("Backend:", "C#, .NET (ASP.NET Core), ABP Framework, Entity Framework Core, REST API"),
            ("Xác thực &amp; Bảo mật:", "OpenID Connect / OAuth2, PKCE, client credentials, RBAC, nhật ký kiểm toán"),
            ("Dữ liệu:", "SQL Server (T-SQL, migration), PostgreSQL, ClickHouse, kiểm tra dữ liệu"),
            ("Tích hợp:", "API service-to-service, đồng bộ dữ liệu, webhook"),
            ("Chất lượng &amp; Vận hành:", "xUnit, cổng kiểm thử CI, Docker, Linux, giám sát"),
            ("Bổ trợ:", "React + TypeScript, Python, Rust"),
        ],
        "exp_en": [
            "Designed and shipped .NET APIs for production platforms: enterprise reporting (import &amp; "
            "validation, approval workflows) and project data management.",
            "Built domain, data and API layers: ABP modules, EF Core + SQL Server schemas and migrations, "
            "REST endpoints for SPAs and other systems.",
            "Implemented central authentication: OpenID Connect / OAuth2, PKCE, client credentials, "
            "role-based access, session and audit tracking.",
            "Delivered service-to-service integrations and a data lakehouse backend (Python, ClickHouse, "
            "Rust parsing core); wired xUnit and integration tests into CI.",
        ],
        "exp_vi": [
            "Thiết kế và phát triển API .NET cho các nền tảng production: báo cáo doanh nghiệp (nhập &amp; "
            "kiểm tra dữ liệu, quy trình duyệt) và quản lý dữ liệu dự án.",
            "Xây dựng tầng domain, dữ liệu và API: module ABP, schema &amp; migration EF Core + SQL Server, "
            "REST endpoint cho SPA và hệ thống khác.",
            "Triển khai xác thực tập trung: OpenID Connect / OAuth2, PKCE, client credentials, phân quyền "
            "theo vai trò, theo dõi phiên và kiểm toán.",
            "Xây dựng tích hợp service-to-service và backend data lakehouse (Python, ClickHouse, lõi Rust); "
            "đưa test xUnit và integration test vào CI.",
        ],
        "projects_en": [
            ("Enterprise reporting platform", "ABP / .NET · EF Core · SQL Server",
             ["Import &amp; validation pipeline, approval workflows and reporting APIs."]),
            ("Central authentication (SSO) service", "ABP / .NET · OpenID Connect · SQL Server",
             ["OIDC flows, RBAC, session &amp; audit tracking, user-lookup APIs for other systems."]),
            ("Project data platform", "ABP / .NET · EF Core · SQL Server · Docker",
             ["APIs for coordination, member invitations and master-data sync."]),
        ],
        "projects_vi": [
            ("Nền tảng báo cáo doanh nghiệp", "ABP / .NET · EF Core · SQL Server",
             ["Pipeline nhập &amp; kiểm tra dữ liệu, quy trình duyệt và API báo cáo."]),
            ("Dịch vụ xác thực tập trung (SSO)", "ABP / .NET · OpenID Connect · SQL Server",
             ["Luồng OIDC, RBAC, theo dõi phiên &amp; kiểm toán, API tra cứu người dùng cho hệ thống khác."]),
            ("Nền tảng dữ liệu dự án", "ABP / .NET · EF Core · SQL Server · Docker",
             ["API điều phối, mời thành viên và đồng bộ dữ liệu danh mục."]),
        ],
    },
    {
        "id": "frontend-react",
        "file": "FrontendReact",
        "title_en": "Frontend Developer — React / TypeScript",
        "title_vi": "Lập trình viên Frontend — React / TypeScript",
        "badge_vi": "LẬP TRÌNH VIÊN FRONTEND",
        "summary_en": (
            "Frontend developer with 1.5 years building React + TypeScript applications. Ships data-dense "
            "internal UIs (dashboards, tables, multi-step import and approval flows) with clean components, "
            "vi/en i18n and automated tests. Integrates SPA authentication via OpenID Connect and works "
            "comfortably with .NET APIs."
        ),
        "summary_vi": (
            "Lập trình viên frontend với 1,5 năm xây dựng ứng dụng React + TypeScript. Phát triển giao diện "
            "nội bộ dày dữ liệu (dashboard, bảng, luồng nhập &amp; duyệt nhiều bước) với component rõ ràng, "
            "đa ngôn ngữ vi/en và kiểm thử tự động. Tích hợp xác thực SPA qua OpenID Connect, làm việc tốt "
            "với API .NET."
        ),
        "skills_en": [
            ("Frontend:", "React, TypeScript, JavaScript, Svelte, Vite, HTML5, CSS3, responsive design"),
            ("UI patterns:", "Dashboards &amp; data tables, multi-step forms, i18n (vi/en), theming"),
            ("Auth:", "OIDC SPA integration (PKCE), token renewal, session-expiry UX"),
            ("Testing:", "Vitest, Playwright (end-to-end), component tests"),
            ("Backend &amp; Tools:", "REST APIs, C# / .NET basics, Node.js, pnpm, Git, Docker"),
        ],
        "skills_vi": [
            ("Frontend:", "React, TypeScript, JavaScript, Svelte, Vite, HTML5, CSS3, responsive design"),
            ("Mẫu giao diện:", "Dashboard &amp; bảng dữ liệu, form nhiều bước, i18n (vi/en), theming"),
            ("Xác thực:", "Tích hợp OIDC cho SPA (PKCE), gia hạn token, xử lý hết phiên"),
            ("Kiểm thử:", "Vitest, Playwright (end-to-end), component test"),
            ("Backend &amp; Công cụ:", "REST API, C# / .NET cơ bản, Node.js, pnpm, Git, Docker"),
        ],
        "exp_en": [
            "Built React + TypeScript UIs for reporting and project-data platforms: dashboards, filterable "
            "tables, import wizards and approval flows.",
            "Built a Svelte portal for a data lakehouse; refactored large screens into small reusable "
            "components with no behaviour change.",
            "Integrated SPA authentication with OpenID Connect (PKCE), silent renewal and role-based UI.",
            "Wrote Vitest and Playwright tests and ran them as CI gates; added vi/en internationalisation.",
        ],
        "exp_vi": [
            "Xây dựng giao diện React + TypeScript cho nền tảng báo cáo và dữ liệu dự án: dashboard, bảng có "
            "bộ lọc, wizard nhập liệu và luồng duyệt.",
            "Xây dựng portal Svelte cho data lakehouse; tách màn hình lớn thành component nhỏ tái sử dụng, "
            "không đổi hành vi.",
            "Tích hợp xác thực SPA với OpenID Connect (PKCE), gia hạn token ngầm và giao diện theo vai trò.",
            "Viết test Vitest và Playwright chạy như cổng CI; bổ sung đa ngôn ngữ vi/en.",
        ],
        "projects_en": [
            ("Enterprise reporting UI", "React · TypeScript · Vite",
             ["Dashboards, import wizards and approval screens for accounting teams."]),
            ("Data portal", "Svelte · TypeScript · Playwright",
             ["Role-aware portal with charts, exports and end-to-end tests."]),
            ("Project data UI", "React · TypeScript · Vite",
             ["Coordination workspace, member invitations and master-data screens."]),
        ],
        "projects_vi": [
            ("Giao diện báo cáo doanh nghiệp", "React · TypeScript · Vite",
             ["Dashboard, wizard nhập liệu và màn duyệt cho khối kế toán."]),
            ("Portal dữ liệu", "Svelte · TypeScript · Playwright",
             ["Portal theo vai trò với biểu đồ, xuất báo cáo và test end-to-end."]),
            ("Giao diện dữ liệu dự án", "React · TypeScript · Vite",
             ["Không gian điều phối, mời thành viên và màn dữ liệu danh mục."]),
        ],
    },
    {
        "id": "devops",
        "file": "DevOps",
        "title_en": "DevOps Engineer — Docker / Linux / CI-CD",
        "title_vi": "Kỹ sư DevOps — Docker / Linux / CI-CD",
        "badge_vi": "KỸ SƯ DEVOPS",
        "summary_en": (
            "DevOps-minded engineer with 1.5 years running internal platforms across dev / UAT / production "
            "on Docker &amp; Linux: CI/CD, reverse proxy &amp; TLS, monitoring and alerting, backups and "
            "rollback-safe releases. Also develops on the stack (.NET / React / Python)."
        ),
        "summary_vi": (
            "Kỹ sư thiên về DevOps với 1,5 năm vận hành nền tảng nội bộ trên dev / UAT / production với "
            "Docker &amp; Linux: CI/CD, reverse proxy &amp; TLS, giám sát và cảnh báo, backup và phát hành "
            "có rollback. Đồng thời phát triển trên stack (.NET / React / Python)."
        ),
        "skills_en": [
            ("Containers &amp; OS:", "Docker, Docker Compose, Linux (Ubuntu), WSL, Bash"),
            ("CI/CD:", "Git, pipeline automation, test gates, security scans, versioned releases &amp; rollback"),
            ("Networking:", "Nginx, reverse proxy, DNS &amp; TLS, VPN, SSO-protected access"),
            ("Observability:", "Prometheus, Grafana, alerting, health checks"),
            ("Data operations:", "SQL Server / PostgreSQL / ClickHouse backup &amp; restore, maintenance automation"),
            ("Development:", "C# / .NET, React + TypeScript, Python, Rust"),
        ],
        "skills_vi": [
            ("Container &amp; OS:", "Docker, Docker Compose, Linux (Ubuntu), WSL, Bash"),
            ("CI/CD:", "Git, tự động hóa pipeline, cổng kiểm thử, quét bảo mật, phát hành theo version &amp; rollback"),
            ("Mạng:", "Nginx, reverse proxy, DNS &amp; TLS, VPN, truy cập bảo vệ bằng SSO"),
            ("Giám sát:", "Prometheus, Grafana, cảnh báo, health check"),
            ("Vận hành dữ liệu:", "Backup &amp; restore SQL Server / PostgreSQL / ClickHouse, tự động hóa bảo trì"),
            ("Phát triển:", "C# / .NET, React + TypeScript, Python, Rust"),
        ],
        "exp_en": [
            "Built and operated the delivery platform for several systems across dev / UAT / production: "
            "Dockerized services and CI/CD with build, test, scan and deploy stages.",
            "Ran the access layer: reverse proxy with TLS, SSO-protected tools and VPN access.",
            "Set up monitoring and alerting (Prometheus, Grafana), health checks with auto-restart, "
            "scheduled backups with restore drills and capacity cleanup.",
            "Cut CI test time by ~65% via sharded parallel jobs; automated maintenance with Python / Bash.",
        ],
        "exp_vi": [
            "Xây dựng và vận hành nền tảng phát hành cho nhiều hệ thống trên dev / UAT / production: dịch vụ "
            "Docker và CI/CD gồm các bước build, test, quét, deploy.",
            "Vận hành tầng truy cập: reverse proxy với TLS, công cụ bảo vệ bằng SSO và VPN.",
            "Thiết lập giám sát và cảnh báo (Prometheus, Grafana), health check tự restart, backup định kỳ "
            "kèm diễn tập restore và dọn dung lượng.",
            "Giảm ~65% thời gian test CI nhờ chia shard song song; tự động hóa bảo trì bằng Python / Bash.",
        ],
        "projects_en": [
            ("Delivery platform &amp; environments", "Docker · CI/CD · Reverse proxy · Linux",
             ["Multi-environment release pipeline with test gates, versioned images and rollback."]),
            ("Observability &amp; backups", "Prometheus · Grafana · Bash",
             ["Dashboards, alerts, scheduled backups and restore drills."]),
            ("Maintenance automation", "Python · Bash · WSL",
             ["Scheduled cleanup and maintenance jobs for internal platforms."]),
        ],
        "projects_vi": [
            ("Nền tảng phát hành &amp; môi trường", "Docker · CI/CD · Reverse proxy · Linux",
             ["Pipeline phát hành đa môi trường với cổng kiểm thử, image theo version và rollback."]),
            ("Giám sát &amp; backup", "Prometheus · Grafana · Bash",
             ["Dashboard, cảnh báo, backup định kỳ và diễn tập restore."]),
            ("Tự động hóa bảo trì", "Python · Bash · WSL",
             ["Job dọn dẹp và bảo trì định kỳ cho nền tảng nội bộ."]),
        ],
    },
    {
        "id": "ai-automation",
        "file": "AIAutomation",
        "title_en": "AI &amp; Automation Engineer — Python / LLM APIs",
        "title_vi": "Kỹ sư AI &amp; Tự động hóa — Python / LLM API",
        "badge_vi": "KỸ SƯ AI &amp; TỰ ĐỘNG HÓA",
        "summary_en": (
            "AI graduate (B.Sc. Artificial Intelligence) and automation engineer with 1.5 years of "
            "experience. Builds Python workflows that combine LLM APIs with data processing to automate "
            "internal operations, and ships the surrounding software (.NET / React) and infrastructure "
            "(Docker, CI/CD, monitoring)."
        ),
        "summary_vi": (
            "Tốt nghiệp ngành Trí tuệ nhân tạo, kỹ sư tự động hóa với 1,5 năm kinh nghiệm. Xây dựng quy "
            "trình Python kết hợp LLM API với xử lý dữ liệu để tự động hóa vận hành nội bộ, đồng thời phát "
            "triển phần mềm xung quanh (.NET / React) và hạ tầng (Docker, CI/CD, giám sát)."
        ),
        "skills_en": [
            ("AI &amp; LLM:", "LLM API integration, prompt &amp; workflow design, automation pipelines; AI/ML fundamentals"),
            ("Python:", "Automation scripts, data processing (Pandas, NumPy), REST API integration"),
            ("Data:", "SQL, PostgreSQL, ClickHouse, Excel data handling, validation pipelines"),
            ("Software:", "C# / .NET, React + TypeScript, Rust, REST APIs"),
            ("Operations:", "Docker, Linux / WSL, CI/CD, monitoring, backups"),
        ],
        "skills_vi": [
            ("AI &amp; LLM:", "Tích hợp LLM API, thiết kế prompt &amp; workflow, pipeline tự động hóa; nền tảng AI/ML"),
            ("Python:", "Script tự động hóa, xử lý dữ liệu (Pandas, NumPy), tích hợp REST API"),
            ("Dữ liệu:", "SQL, PostgreSQL, ClickHouse, xử lý dữ liệu Excel, pipeline kiểm tra dữ liệu"),
            ("Phần mềm:", "C# / .NET, React + TypeScript, Rust, REST API"),
            ("Vận hành:", "Docker, Linux / WSL, CI/CD, giám sát, backup"),
        ],
        "exp_en": [
            "Built Python + LLM API automation pipelines for data extraction and processing, removing "
            "repetitive manual work for management teams.",
            "Added AI-generated narrative analysis to a data portal, with rule-based fallback when the "
            "model is unavailable.",
            "Engineered data pipelines (Bronze / Silver / Gold) with a Rust parsing core: import, "
            "validation and per-row error reporting.",
            "Delivered the surrounding software and infrastructure: .NET APIs, React UIs, SSO, Docker, "
            "CI/CD and monitoring.",
        ],
        "exp_vi": [
            "Xây dựng pipeline tự động hóa Python + LLM API để trích xuất và xử lý dữ liệu, loại bỏ việc "
            "thủ công lặp lại cho bộ phận quản lý.",
            "Bổ sung phân tích văn bản do AI sinh vào portal dữ liệu, có phương án dự phòng theo quy tắc "
            "khi mô hình không khả dụng.",
            "Xây dựng pipeline dữ liệu (Bronze / Silver / Gold) với lõi Rust: nhập, kiểm tra và báo lỗi "
            "theo từng dòng.",
            "Phát triển phần mềm và hạ tầng xung quanh: API .NET, giao diện React, SSO, Docker, CI/CD và "
            "giám sát.",
        ],
        "projects_en": [
            ("LLM automation pipelines", "Python · LLM APIs · WSL",
             ["Automated data extraction and processing workflows for management teams."]),
            ("Data pipeline &amp; lakehouse", "Python · Rust · ClickHouse · PostgreSQL",
             ["Import, validation and analytics pipeline with AI narrative and automated tests."]),
            ("Platform engineering", ".NET · React · Docker · CI/CD",
             ["Authentication, reporting and project-data platforms shipped to production."]),
        ],
        "projects_vi": [
            ("Pipeline tự động hóa với LLM", "Python · LLM API · WSL",
             ["Tự động hóa trích xuất và xử lý dữ liệu cho bộ phận quản lý."]),
            ("Pipeline dữ liệu &amp; lakehouse", "Python · Rust · ClickHouse · PostgreSQL",
             ["Pipeline nhập, kiểm tra, phân tích kèm nhận định AI và kiểm thử tự động."]),
            ("Kỹ thuật nền tảng", ".NET · React · Docker · CI/CD",
             ["Nền tảng xác thực, báo cáo và dữ liệu dự án đã lên production."]),
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
<html lang="{{LANG}}">
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
  <h2>{{H_SUMMARY}}</h2>
  <p>{{SUMMARY}}</p>
  <h2>{{H_SKILLS}}</h2>
  <div class="skills">{{SKILLS}}</div>
  <h2>{{H_EXP}}</h2>
  <div>
    <p class="role">{{JOB}}</p>
    <p class="meta">{{JOB_META}}</p>
    <ul>{{BULLETS}}</ul>
  </div>
  <h2>{{H_PROJ}}</h2>
  {{PROJECTS}}
  <h2>{{H_EDU}}</h2>
  <p>{{EDUCATION}} &nbsp;·&nbsp; {{LANGUAGES}}</p>
</div>
</body>
</html>
"""

VISUAL_HTML = r"""<!DOCTYPE html>
<html lang="{{LANG}}">
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
      <img src="{{AVATAR}}" alt="{{NAME}}" class="profile-img">
    </div>
    <div class="name-title-container">
      <h1>{{NAME}}</h1>
      <div class="job-badge">{{BADGE}}</div>
    </div>
    <div class="sidebar-section">
      <h2>{{H_CONTACT}}</h2>
      <ul class="contact-list">{{CONTACTS}}</ul>
    </div>
    <div class="sidebar-section">
      <h2>{{H_SUMMARY}}</h2>
      <p class="sidebar-text">{{SUMMARY}}</p>
    </div>
    <div class="sidebar-section">
      <h2>{{H_EDU_V}}</h2>
      <div class="education-item">{{EDUCATION}}</div>
    </div>
    <div class="sidebar-section">
      <h2>{{H_LANG_V}}</h2>
      <ul class="lang-list">{{LANGUAGES}}</ul>
    </div>
  </div>
  <div class="main-content">
    <div class="main-section">
      <h2>{{H_EXP}}</h2>
      <div>
        <div class="experience-header">
          <span class="experience-title">{{JOB_TITLE}}</span>
          <span class="company-name">{{COMPANY}}</span>
        </div>
        <div class="job-date">{{JOB_META}}</div>
        <ul class="bullet-list">{{BULLETS}}</ul>
      </div>
    </div>
    <div class="main-section">
      <h2>{{H_PROJ}}</h2>
      {{PROJECTS}}
    </div>
    <div class="main-section">
      <h2>{{H_SKILLS}}</h2>
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


def render_contacts_visual(lang="VI"):
    out = []
    contacts = CONTACT_VI if lang == "VI" else [("pin", CONTACT_EN_PIN)] + CONTACT_VI[1:]
    for kind, text in contacts:
        out.append(f"        <li>{CONTACT_SVGS[kind]}<span>{text}</span></li>")
    return "\n".join(out)


LABELS = {
    "EN": dict(lang="en", summary="Summary", skills="Core Skills", exp="Professional Experience",
               proj="Selected Projects", edu="Education &amp; Languages", contact="CONTACT",
               skills_v="TECHNICAL SKILLS", exp_v="EXPERIENCE", proj_v="SELECTED PROJECTS",
               summary_v="SUMMARY", edu_v="EDUCATION", lang_v="LANGUAGES",
               job_title="Web &amp; Database Developer", company="HOAN CAU GROUP",
               langs="<li><strong>Vietnamese:</strong> Native</li><li><strong>English:</strong> Elementary</li>"),
    "VI": dict(lang="vi", summary="Tóm tắt", skills="Kỹ năng", exp="Kinh nghiệm làm việc",
               proj="Dự án tiêu biểu", edu="Học vấn &amp; Ngôn ngữ", contact="LIÊN HỆ",
               skills_v="KỸ NĂNG CHUYÊN MÔN", exp_v="KINH NGHIỆM LÀM VIỆC", proj_v="DỰ ÁN TIÊU BIỂU",
               summary_v="TÓM TẮT", edu_v="HỌC VẤN", lang_v="NGÔN NGỮ",
               job_title="Lập trình viên Web &amp; Cơ sở dữ liệu", company="TẬP ĐOÀN HOÀN CẦU",
               langs="<li><strong>Tiếng Việt:</strong> Bản ngữ</li><li><strong>Tiếng Anh:</strong> Cơ bản</li>"),
}
CONTACT_EN_PIN = "Ho Chi Minh City, Vietnam"


def default_ctx(lang):
    """Thông tin người dùng mặc định (Vũ Hữu Đô). cvtui.py truyền ctx riêng cho từng hồ sơ."""
    en = lang == "EN"
    return dict(
        name=NAME_EN if en else NAME_VI, avatar="Avatar.png", contact_line=CONTACT_LINE,
        contacts=[("pin", CONTACT_EN_PIN if en else CONTACT_VI[0][1])] + CONTACT_VI[1:],
        job=JOB_EN if en else JOB_VI, job_meta=JOB_META_EN if en else JOB_META_VI,
        job_title=LABELS[lang]["job_title"], company=LABELS[lang]["company"],
        education=EDUCATION_EN if en else EDUCATION_VI,
        languages=LANGUAGES_EN if en else LANGUAGES_VI, langs_li=LABELS[lang]["langs"])


def build_html(role, lang, kind=None, name=None, ctx=None):
    """kind: 'ats' (1 cột, máy đọc) | 'human' (2 cột, người đọc). Mặc định cũ: EN=ats, VI=human."""
    kind = kind or ("ats" if lang == "EN" else "human")
    k = lang.lower()
    L = LABELS[lang]
    ctx = ctx or default_ctx(lang)
    name = name or ctx["name"]
    title = role["title_" + k]
    common = {
        "{{LANG}}": L["lang"], "{{NAME}}": name, "{{TITLE}}": title,
        "{{SUMMARY}}": role["summary_" + k],
        "{{BULLETS}}": render_bullets(role["exp_" + k]),
        "{{EDUCATION}}": ctx["education"],
        "{{JOB_META}}": ctx["job_meta"],
        "{{H_SUMMARY}}": L["summary"] if kind == "ats" else L["summary_v"],
        "{{H_SKILLS}}": L["skills"] if kind == "ats" else L["skills_v"],
        "{{H_EXP}}": L["exp"] if kind == "ats" else L["exp_v"],
        "{{H_PROJ}}": L["proj"] if kind == "ats" else L["proj_v"],
        "{{H_EDU}}": L["edu"],
    }
    if kind == "ats":
        html = ATS_HTML
        repl = dict(common, **{
            "{{CONTACT}}": ctx["contact_line"],
            "{{SKILLS}}": render_skills_ats(role["skills_" + k]),
            "{{JOB}}": ctx["job"],
            "{{PROJECTS}}": render_projects_ats(role["projects_" + k]),
            "{{LANGUAGES}}": ctx["languages"],
        })
    else:
        html = VISUAL_HTML
        repl = dict(common, **{
            "{{AVATAR}}": ctx["avatar"], "{{BADGE}}": role.get("badge_" + k) or title.upper(),
            "{{CONTACTS}}": "\n".join(f"        <li>{CONTACT_SVGS[k]}<span>{t}</span></li>" for k, t in ctx["contacts"]),
            "{{SKILLS}}": render_skills_visual(role["skills_" + k]),
            "{{PROJECTS}}": render_projects_visual(role["projects_" + k]),
            "{{LANGUAGES}}": ctx["langs_li"],
            "{{H_CONTACT}}": L["contact"], "{{H_EDU_V}}": L["edu_v"], "{{H_LANG_V}}": L["lang_v"],
            "{{JOB_TITLE}}": ctx["job_title"], "{{COMPANY}}": ctx["company"],
        })
    for key, value in repl.items():
        html = html.replace(key, value)
    if kind != "ats" and not ctx["avatar"]:
        html = re.sub(r'<div class="profile-img-container">.*?</div>', "", html, flags=re.S)
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
