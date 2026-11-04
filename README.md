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

## TUI tạo CV theo role (nhiều người dùng)

```bash
uv run cvtui.py --new <id>          # tạo hồ sơ profiles/<id>/profile.json từ mẫu, rồi sửa file đó
uv run cvtui.py                     # TUI: chọn hồ sơ, nhập role (+ dán JD), tuỳ chỉnh tên/chức danh/ảnh -> Ctrl+G
uv run cvtui.py --profile <id> --role "DevOps Engineer" --jd jd.txt --lang EN,VI \
    [--title "Senior DevOps"] [--name "..."] [--avatar ~/anh.jpg]
uv run cvtui.py --list | --check
```

Mỗi lần ra 2 loại, đều 1 trang A4, lưu ở `out/<id>/<role>/` (không commit):
- `*_Human.pdf`: 2 cột, có ảnh, nộp cho người đọc.
- `*_ATS.pdf`: 1 cột, chữ thuần, nộp cho máy đọc.

- Nội dung chọn từ `profiles/<id>/profile.json` theo độ khớp với role/JD (từ khóa ở `taxonomy.json`, dùng chung). Kỹ năng JD đòi mà hồ sơ chưa có chỉ được **báo thiếu**, không tự thêm vào CV.
- `profiles/<id>/denylist.txt` (mỗi dòng 1 từ cấm): CV nào chứa từ cấm sẽ bị báo `RÒ RỈ`, lệnh trả mã lỗi 1.
- Hồ sơ người dùng, `denylist.txt` và `out/` đều đã `.gitignore`. Chỉ `_template` và hồ sơ mẫu `vuhuudo` được commit.
- Hướng dẫn viết CV an toàn: [`docs/CV_GUIDE.md`](docs/CV_GUIDE.md). Quy trình cho AI agent: [`AGENTS.md`](AGENTS.md).

## Ghi chú

- **Nội dung CV theo role nằm trong `build_cvs.py`** (mục `ROLES`) — sửa ở đó rồi chạy `uv run build_cvs.py`; script sẽ **ghi đè** HTML/PDF trong `roles/`. Muốn thêm role mới: copy một mục trong `ROLES`, đổi `id`/`file`/nội dung.
- Bản `_ATS` (và bản `_EN` của roles) không dùng cột/icon/ảnh — an toàn khi máy đọc CV tự động.
- CV chỉ mô tả chung (không nêu tên hệ thống nội bộ, số liệu đơn vị, hạ tầng); repo công khai nên không thêm chi tiết nội bộ.
- Nên đặt LinkedIn custom URL (vd: `linkedin.com/in/vuhuudo`) rồi cập nhật lại trong CV.
