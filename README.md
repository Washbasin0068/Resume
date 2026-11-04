# Resume — Vũ Hữu Đô (Vu Huu Do)

CV của **Vũ Hữu Đô** — Full Stack Developer (.NET / React), TP. Hồ Chí Minh.

## CV chính (full-stack)

| Tệp | Dùng khi nào |
|---|---|
| `CV_VuHuuDo_FullStack.pdf` | Bản đẹp 2 cột (tiếng Anh) — gửi email, gặp trực tiếp |
| `CV_VuHuuDo_FullStack_ATS.pdf` | Bản 1 cột tối giản (tiếng Anh) — gửi qua hệ thống tuyển dụng (ATS), LinkedIn, TopCV/ITviec |
| `CV_VuHuuDo_VI.pdf` | Bản tiếng Việt 2 cột — gửi nhà tuyển dụng Việt Nam |
| `CV_VuHuuDo_LinkedIn.pdf` | Bản export từ LinkedIn (giữ nguyên để tham chiếu) |

## CV theo role — `roles/`

Mỗi role có 2 bản: **`_EN.pdf`** (1 cột, thân thiện ATS) và **`_VI.pdf`** (2 cột, tiếng Việt).

| Thư mục | Vị trí ứng tuyển |
|---|---|
| `roles/software-engineer/` | Software Engineer (tổng quát, full stack & platform) |
| `roles/backend-dotnet/` | Backend Developer (.NET / C#) |
| `roles/frontend-react/` | Frontend Developer (React / TypeScript) |
| `roles/devops/` | DevOps Engineer (Docker / Linux / CI-CD) |
| `roles/ai-automation/` | AI & Automation Engineer (Python / LLM APIs) |

## Cấu trúc

```
├── CV_VuHuuDo_FullStack.pdf        # sinh từ html/CV_FullStackDev.html
├── CV_VuHuuDo_FullStack_ATS.pdf    # sinh từ html/CV_FullStackDev_ATS.html
├── CV_VuHuuDo_VI.pdf               # sinh từ html/CV_VuHuuDo_VI.html
├── CV_VuHuuDo_LinkedIn.pdf         # export từ LinkedIn
├── build.sh                        # build toàn bộ (CV chính + roles/)
├── build_cvs.py                    # sinh CV theo role từ dữ liệu trong script
├── roles/
│   ├── software-engineer/          # CV_VuHuuDo_SoftwareEngineer_{EN,VI}.{html,pdf}
│   ├── backend-dotnet/             # CV_VuHuuDo_BackendDotNet_{EN,VI}.{html,pdf}
│   ├── frontend-react/             # CV_VuHuuDo_FrontendReact_{EN,VI}.{html,pdf}
│   ├── devops/                     # CV_VuHuuDo_DevOps_{EN,VI}.{html,pdf}
│   └── ai-automation/              # CV_VuHuuDo_AIAutomation_{EN,VI}.{html,pdf}
└── html/
    ├── CV_FullStackDev.html        # nguồn bản EN (2 cột)
    ├── CV_FullStackDev_ATS.html    # nguồn bản EN (1 cột, ATS)
    ├── CV_VuHuuDo_VI.html          # nguồn bản VI (2 cột)
    └── Avatar.png
```

## Build lại PDF

Yêu cầu: Chromium (hoặc Chrome) + uv + Python (`pdfinfo` tuỳ chọn, để kiểm tra số trang).

```bash
./build.sh              # build tất cả: CV chính + roles/
uv run build_cvs.py    # chỉ build lại CV theo role
```

Hoặc in thủ công: mở file HTML bằng Chrome/Chromium → Print → Save as PDF (khổ A4, margins theo CSS `@media print`).

## TUI tạo CV theo role

```bash
uv run cvtui.py                                   # mở TUI: nhập role (+ dán JD) -> Ctrl+G
uv run cvtui.py --role "DevOps Engineer" --jd jd.txt --lang EN,VI   # không TUI
uv run cvtui.py --check                           # tự kiểm tra
```

Mỗi lần ra 2 loại, đều 1 trang A4, lưu ở `out/<role>/` (không commit):
- `*_Human.pdf` — 2 cột, có ảnh, nộp cho người đọc.
- `*_ATS.pdf` — 1 cột, chữ thuần, nộp cho máy đọc.

Nội dung chọn từ `profile.json` (ngân hàng nội dung) theo độ khớp với role/JD. Kỹ năng JD đòi mà profile chưa có chỉ được **báo thiếu**, không tự thêm vào CV. Muốn thêm kinh nghiệm/kỹ năng: sửa `profile.json` (viết chung chung, không nêu thông tin nội bộ).

## Ghi chú

- **Nội dung CV theo role nằm trong `build_cvs.py`** (mục `ROLES`) — sửa ở đó rồi chạy `uv run build_cvs.py`; script sẽ **ghi đè** HTML/PDF trong `roles/`. Muốn thêm role mới: copy một mục trong `ROLES`, đổi `id`/`file`/nội dung.
- Bản `_ATS` (và bản `_EN` của roles) không dùng cột/icon/ảnh — an toàn khi máy đọc CV tự động.
- CV chỉ mô tả chung (không nêu tên hệ thống nội bộ, số liệu đơn vị, hạ tầng); repo công khai nên không thêm chi tiết nội bộ.
- Nên đặt LinkedIn custom URL (vd: `linkedin.com/in/vuhuudo`) rồi cập nhật lại trong CV.
