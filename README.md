# Resume — Vũ Hữu Đô (Vu Huu Do)

CV của **Vũ Hữu Đô** — Full Stack Developer (.NET / React), TP. Hồ Chí Minh.

## Các bản CV

| Tệp | Dùng khi nào |
|---|---|
| `CV_VuHuuDo_FullStack.pdf` | Bản đẹp 2 cột (tiếng Anh) — gửi email, gặp trực tiếp |
| `CV_VuHuuDo_FullStack_ATS.pdf` | Bản 1 cột tối giản (tiếng Anh) — gửi qua hệ thống tuyển dụng (ATS), LinkedIn, TopCV/ITviec |
| `CV_VuHuuDo_VI.pdf` | Bản tiếng Việt 2 cột — gửi nhà tuyển dụng Việt Nam |
| `CV_VuHuuDo_LinkedIn.pdf` | Bản export từ LinkedIn (giữ nguyên để tham chiếu) |

## Cấu trúc

```
├── CV_VuHuuDo_FullStack.pdf        # sinh từ html/CV_FullStackDev.html
├── CV_VuHuuDo_FullStack_ATS.pdf    # sinh từ html/CV_FullStackDev_ATS.html
├── CV_VuHuuDo_VI.pdf               # sinh từ html/CV_VuHuuDo_VI.html
├── CV_VuHuuDo_LinkedIn.pdf         # export từ LinkedIn
├── build.sh                        # build lại toàn bộ PDF
└── html/
    ├── CV_FullStackDev.html        # nguồn bản EN (2 cột)
    ├── CV_FullStackDev_ATS.html    # nguồn bản EN (1 cột, ATS)
    ├── CV_VuHuuDo_VI.html          # nguồn bản VI (2 cột)
    ├── Web_resume.html             # bản 1 cột cũ (đã thay bằng bản _ATS)
    └── Avatar.png
```

## Build lại PDF

Yêu cầu: Chromium (hoặc Chrome) cài sẵn.

```bash
./build.sh
```

Hoặc in thủ công: mở file HTML bằng Chrome/Chromium → Print → Save as PDF (khổ A4, margins theo CSS `@media print`).

## Ghi chú

- Bản `_ATS` không dùng cột/icon/ảnh — an toàn khi máy đọc CV tự động.
- Khi cập nhật nội dung: sửa file HTML trong `html/`, chạy `./build.sh`, rồi commit cả HTML lẫn PDF.
- Nên đặt LinkedIn custom URL (vd: `linkedin.com/in/vuhuudo`) rồi cập nhật lại trong CV.
