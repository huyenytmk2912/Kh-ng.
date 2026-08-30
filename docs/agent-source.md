# Agent source snapshot

Nguồn tham khảo: repository `huyenytmk2912/1`, branch `main`.

Agent ở dự án `1` hiện là một scaffold web để khởi động/dừng một process Node (`agent/agent.js`) qua API `/api/start` và `/api/stop`. `web/server.js` đọc `MESSAGE`, `COUNT`, `DELAY` từ request rồi spawn agent process. README mô tả luồng tự động nhập/gửi tin nhắn qua accessibility/UI semantics và computer vision fallback.

Khuong sẽ không sao chép mù runtime này. Nội dung được tách thành các contract/tool capability phù hợp với runtime Python của Khuong, giữ sandbox/permission boundary ở host.
