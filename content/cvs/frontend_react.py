"""CV Frontend Developer (React / TypeScript)."""
CV = {
    "id": "frontend-react",
    "file": "FrontendReact",
    "outputs": [("en", "ats"), ("vi", "visual")],

    "title_en": "Frontend Developer — React / TypeScript",
    "title_vi": "Lập trình viên Frontend — React / TypeScript",
    "badge_en": "FRONTEND DEVELOPER",
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
        "Phủ kiểm thử tự động cho giao diện — Vitest (unit) và Playwright (E2E) — chạy trong CI cùng API "
        ".NET.",
        "Làm việc trọn vòng với API .NET và dữ liệu SQL; tự động hóa bằng Python + Gemini API; chủ trì "
        "triển khai Base.vn (hội sở HCM, chi nhánh Khánh Hòa).",
    ],

    "projects_en": [
        ("Multi-company financial &amp; fund reporting platform (React SPA)",
         "React · TypeScript · Vite · REST APIs",
         ["Dashboards and data-dense tables for 44 companies; period &amp; company navigation; MISA import "
          "and approval flows.",
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
         ["Dashboard và bảng dữ liệu dày đặc cho 44 công ty; điều hướng theo kỳ &amp; công ty; luồng nhập "
          "và duyệt sổ MISA.",
          "Đa ngôn ngữ vi/en, theme và layout responsive; kiểm thử Vitest + Playwright."]),
        ("SSO tập trung — tích hợp SPA",
         "OIDC (PKCE) · React · TypeScript",
         ["Luồng authorization-code + PKCE, gia hạn token ngầm và xử lý hết phiên cho các SPA nội bộ."]),
        ("Nền tảng dữ liệu dự án xây dựng (giao diện React)",
         "React · TypeScript · Vite",
         ["Không gian điều phối, mời thành viên và màn Master Data; đã phát hành production."]),
    ],
}
