# CV — Vũ Hữu Đô (Vu Huu Do)

Bộ CV đa phiên bản cho **Vũ Hữu Đô** — Full Stack Developer (.NET / React), TP. Hồ Chí Minh.
Nội dung được viết một lần, sinh ra nhiều bản theo **role** và **định dạng** (ATS / visual, EN / VI).

## Nộp ở đâu — dùng file nào

| Ứng tuyển vị trí | Tiếng Anh (ATS) | Tiếng Việt |
|---|---|---|
| Full Stack Developer (.NET / React) | `cv/fullstack/CV_VuHuuDo_FullStack_EN_ATS.pdf` | `cv/fullstack/CV_VuHuuDo_FullStack_VI_Visual.pdf` |
| Software Engineer (tổng quát) | `cv/software-engineer/CV_VuHuuDo_SoftwareEngineer_EN_ATS.pdf` | `cv/software-engineer/CV_VuHuuDo_SoftwareEngineer_VI_Visual.pdf` |
| Backend Developer (.NET / C#) | `cv/backend-dotnet/CV_VuHuuDo_BackendDotNet_EN_ATS.pdf` | `cv/backend-dotnet/CV_VuHuuDo_BackendDotNet_VI_Visual.pdf` |
| Frontend Developer (React / TS) | `cv/frontend-react/CV_VuHuuDo_FrontendReact_EN_ATS.pdf` | `cv/frontend-react/CV_VuHuuDo_FrontendReact_VI_Visual.pdf` |
| DevOps Engineer | `cv/devops/CV_VuHuuDo_DevOps_EN_ATS.pdf` | `cv/devops/CV_VuHuuDo_DevOps_VI_Visual.pdf` |
| AI & Automation Engineer | `cv/ai-automation/CV_VuHuuDo_AIAutomation_EN_ATS.pdf` | `cv/ai-automation/CV_VuHuuDo_AIAutomation_VI_Visual.pdf` |

- **`_EN_ATS.pdf`** — 1 cột, không ảnh/icon: an toàn khi nộp qua hệ thống tuyển dụng (ATS), LinkedIn, ITviec/TopCV.
- **`_VI_Visual.pdf`** — 2 cột, có ảnh: gửi email hoặc gặp trực tiếp nhà tuyển dụng Việt Nam.
- **`cv/fullstack/CV_VuHuuDo_FullStack_EN_Visual.pdf`** — bản EN 2 cột (gửi email cho nhà tuyển dụng nước ngoài).
- **`cv/linkedin/CV_VuHuuDo_LinkedIn.pdf`** — bản export từ LinkedIn (tham chiếu).

## Cấu trúc

```
├── README.md
├── build.sh                  # lệnh build duy nhất: ./build.sh
├── build.py                  # sinh HTML (build/out/) và PDF (cv/)
├── content/                  # NGUỒN NỘI DUNG
│   ├── profile.py            #   thông tin chung: tên, liên hệ, học vấn, ngôn ngữ, nhãn mục
│   └── cvs/                  #   mỗi role một file
│       ├── fullstack.py
│       ├── software_engineer.py
│       ├── backend_dotnet.py
│       ├── frontend_react.py
│       ├── devops.py
│       └── ai_automation.py
├── templates/                # MẪU TRÌNH BÀY (HTML + CSS)
│   ├── ats.html              #   bản 1 cột, tối giản
│   └── visual.html           #   bản 2 cột, sidebar
├── assets/
│   └── avatar.png            # ảnh dùng chung cho mọi bản
├── cv/                       # ĐẦU RA — PDF đã build (commit sẵn để tải/gửi ngay)
└── build/                    # HTML tạm trong lúc build (không commit)
```

## Build lại PDF

Yêu cầu: **Chromium** (hoặc Chrome) + **Python 3** (khuyến nghị **uv**; `pdfinfo` tuỳ chọn để kiểm tra số trang).
Script tự tìm Chrome theo thứ tự: biến `CHROME` → chromium/chrome trong PATH → Chromium của Playwright.

```bash
./build.sh          # tự dùng uv nếu có, không thì python3
uv run build.py     # hoặc chạy trực tiếp (PEP 723, không cần cài thêm gì)
python3 build.py
```

Script build toàn bộ, kiểm tra từng bản **vừa đúng 1 trang** và báo lỗi nếu không.

## Chỉnh sửa nội dung

1. Sửa nội dung trong `content/cvs/<role>.py` (hoặc thông tin chung trong `content/profile.py`).
2. Chạy `./build.sh` — PDF trong `cv/` được cập nhật.
3. Commit cả nội dung lẫn PDF.

**Thêm role mới**: tạo `content/cvs/<role>.py` theo mẫu các file có sẵn, rồi thêm vào danh sách `CVS`
trong `content/cvs/__init__.py`.

## Ghi chú

- CV chỉ **mô tả chung** (không nêu tên hệ thống nội bộ, số liệu đơn vị, hạ tầng); repo công khai nên không thêm chi tiết nội bộ.
- Nên đặt LinkedIn custom URL (vd: `linkedin.com/in/vuhuudo`) rồi cập nhật lại trong `content/profile.py`.
- Nội dung CV là thông tin cá nhân — vui lòng không dùng lại; mã build (`build.py`, `templates/`) tự do tham khảo.
