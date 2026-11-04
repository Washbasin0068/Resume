# Hướng dẫn viết CV: an toàn, trung thực, vẫn được tuyển

Dành cho người dùng và AI agent. Mục tiêu: **thể hiện được năng lực** mà **không lộ thông tin của công ty cũ**.

## 1. Nguyên tắc cốt lõi

> Nhà tuyển dụng thuê **năng lực** của bạn, không thuê **bí mật** của công ty cũ.

Một dòng kinh nghiệm tốt trả lời 3 câu hỏi: **Làm gì?** (động từ mạnh), **bằng gì?** (công nghệ = từ khóa ATS), **kết quả ra sao?** (con số tương đối hoặc trạng thái). Không cần trả lời "của ai, ở đâu, tên gì".

Công thức:

```
[Động từ] + [loại hệ thống chung] + [công nghệ] + [kết quả %, thời gian, trạng thái]
```

## 2. Bài kiểm tra an toàn: mỗi dòng phải qua cả 5

1. **Thay tên công ty** bằng một công ty khác cùng ngành: câu vẫn đúng không? Nếu chỉ đúng với công ty cũ, câu đó quá cụ thể.
2. **Không có tên riêng nội bộ**: tên hệ thống, dự án, khách hàng, đối tác, chi nhánh, server, tên miền, phần mềm nghiệp vụ đặc thù.
3. **Không có số tuyệt đối nhạy cảm**: số công ty con, doanh thu, số khách hàng, số người dùng, số endpoint, ngân sách. Dùng **% hoặc tỷ lệ**.
4. **Không mô tả lỗ hổng/cấu hình bảo mật**: "vá lỗ hổng X ở hệ thống Y", cấu trúc mạng, VPN, cổng, cách phân quyền cụ thể.
5. **Không tiết lộ chiến lược**: kế hoạch kinh doanh, sáp nhập, báo cáo cho ban lãnh đạo về vấn đề gì.

Nếu không chắc, viết chung hơn. Mất một chút chi tiết vẫn tốt hơn mất uy tín, hoặc vi phạm NDA (thỏa thuận bảo mật).

## 3. Viết chung mà vẫn hấp dẫn: trước và sau

Tên trong ví dụ đều là tên giả.


| Lộ thông tin ❌ | An toàn, vẫn hấp dẫn ✅ |
|---|---|
| Built **AcmeLedger** integration for **37 subsidiaries** of **Contoso Group** | Built accounting-system integration for **multi-entity** financial reporting |
| Deployed **OpenVPN on vpn01.contoso.local** for the **Da Nang branch** | Ran secure remote access (**VPN, reverse proxy, TLS**) for regional offices |
| Wrote **96 endpoints** for **Project Falcon** | Designed **REST APIs** with .NET / ABP for a project-data platform in **production** |
| Reported weekly to the **CEO** on the **merger with Fabrikam** | Tracked delivery of cross-team projects and reported progress to management |
| Fixed SQL injection in **portal.company.local** | Hardened web apps: input validation, **RBAC**, audit logging |
| Saved **3 billion VND** per year for **client Northwind** | Removed repetitive manual processing; **cut processing time ~70%** |

Vì sao cột phải vẫn thắng:

- **Từ khóa ATS giữ nguyên**: VPN, TLS, REST API, .NET, RBAC… Máy lọc CV khớp **công nghệ**, không khớp tên dự án nội bộ.
- **Người đọc thấy phạm vi và kết quả**: "multi-entity", "production", "~70%" chứng minh năng lực.
- **Thể hiện sự chuyên nghiệp**: nhà tuyển dụng đánh giá cao người biết giữ bí mật. Họ biết bạn cũng sẽ giữ bí mật cho họ.

## 4. Số liệu an toàn

Dùng được:
- **% cải thiện**: "giảm ~65% thời gian test CI", "tăng ~40% tốc độ truy vấn".
- **Thời gian/quy trình**: "từ 1 ngày xuống 2 giờ", "phát hành hằng tuần thay vì hằng tháng".
- **Trạng thái**: "đã lên production", "dùng hằng ngày bởi nhiều phòng ban", "zero downtime khi nâng cấp".
- **Quy mô dạng khoảng**, nếu thật sự cần: "hàng chục đơn vị", "hàng triệu bản ghi".

Tránh: số tiền, số khách hàng, số người dùng chính xác, số công ty/chi nhánh, tên khách hàng.

Mọi con số phải **giải thích được trong phỏng vấn**: bạn đo thế nào, trước và sau là bao nhiêu. Không nhớ chính xác thì dùng "~" hoặc bỏ số.

## 5. Tên công ty và chức danh

- Tên công ty và chức danh **thường được ghi**, vì nhà tuyển dụng cần để xác minh. Nhưng nếu đang làm ở đó và chưa muốn công khai việc tìm việc, hoặc hợp đồng cấm, hãy dùng mô tả: *"Web & Database Developer — a construction & real-estate group (1,000+ staff)"*.
- Chức danh ghi **đúng chức danh thật**. Không tự nâng "Senior" hay "Lead". Có thể ghi thêm vai trò thực tế trong ngoặc: *"Developer (full-stack, owned CI/CD)"*.

## 6. Tối ưu ATS (máy đọc)

- Dùng bản `*_ATS.pdf`: 1 cột, không bảng, không icon, không ảnh, font chuẩn, tiêu đề mục chuẩn (Summary, Skills, Experience, Projects, Education).
- **Lặp đúng thuật ngữ trong JD** nếu bạn có kỹ năng đó: JD ghi "ASP.NET Core" thì đừng chỉ ghi ".NET". Thêm `m` (alias) trong `profile.json`.
- Ghi cả tên đầy đủ lẫn viết tắt: "OpenID Connect (OIDC)", "Continuous Integration (CI/CD)".
- Từ khóa phải nằm **trong câu kinh nghiệm**, không chỉ ở mục Skills. ATS và người đọc đều tin kinh nghiệm hơn danh sách.
- Không nhồi từ khóa, không giấu chữ trắng.

## 7. Thu hút người đọc

Nhà tuyển dụng đọc lướt CV trong khoảng 6–10 giây. Họ nhìn:
1. **Chức danh dưới tên**: trùng với vị trí đang tuyển. Tool dùng `--title` hoặc role.
2. **Summary 2–3 câu**: số năm + stack chính + 1 thành tựu lớn.
3. **3 dòng kinh nghiệm đầu**: dòng mạnh và khớp JD nhất đặt trên cùng. Tool tự sắp theo độ khớp.
4. **Con số** ở dòng đầu tiên nếu có.

Thêm:
- Động từ mạnh ở đầu câu: Built, Designed, Cut, Automated, Led, Shipped / Xây dựng, Thiết kế, Giảm, Tự động hóa.
- Mỗi role một CV riêng, đừng dùng một CV chung cho mọi vị trí.
- **1 trang** là đủ khi dưới 5 năm kinh nghiệm.
- Link GitHub/portfolio **công khai**, có dự án cá nhân. Đây là nơi an toàn nhất để **khoe code**, thay vì kể chi tiết code của công ty.

## 8. Phần "dự án" khi mọi thứ đều mật

- Mô tả theo **loại hệ thống**: "Enterprise reporting platform", "Central authentication (SSO) service", "Data lakehouse & analytics".
- Tốt hơn nữa: làm **dự án cá nhân** tái hiện kỹ năng (ví dụ một mini SSO bằng OIDC trên GitHub). Có thể nói chi tiết thoải mái vì đó là code của bạn.
- Trong phỏng vấn: nói về **cách tiếp cận, đánh đổi, bài học**, không nói dữ liệu và tên nội bộ. Câu dùng được: *"Phần đó thuộc thỏa thuận bảo mật, nhưng tôi có thể nói về cách tiếp cận…"*.

## 9. Bảo mật dữ liệu cá nhân của chính người dùng

- CV gửi đi chỉ cần: tên, email, số điện thoại, thành phố, LinkedIn/GitHub.
- **Không ghi**: CCCD, ngày sinh, địa chỉ nhà chi tiết, tình trạng hôn nhân, lương.
- Repo CV công khai thì mọi thứ trong đó đều công khai. Hồ sơ thật (`profiles/<id>/`) và `denylist.txt` đã bị `.gitignore`. Muốn lưu, dùng repo **riêng tư**.
- Lịch sử git lưu cả nội dung cũ. Nếu từng commit thông tin mật lên repo công khai, phải viết lại lịch sử (`git filter-repo`) **và** coi như thông tin đó đã lộ.
- PDF có thể chứa metadata (tên tác giả, đường dẫn máy). Kiểm tra bằng `pdfinfo file.pdf`.

## 10. Checklist cuối

- [ ] Mọi file 1 trang (`pdfinfo`).
- [ ] `grep -i -f denylist.txt` trên text PDF không ra gì.
- [ ] Không có tên riêng nội bộ, số tuyệt đối nhạy cảm, URL hay IP nội bộ.
- [ ] Mỗi kỹ năng và con số đều thật, giải thích được trong phỏng vấn.
- [ ] Chức danh dưới tên khớp vị trí ứng tuyển.
- [ ] Bản ATS: `pdftotext` đọc ra đúng thứ tự, đủ mục.
- [ ] Đã báo người dùng các kỹ năng JD đòi mà họ chưa có.
