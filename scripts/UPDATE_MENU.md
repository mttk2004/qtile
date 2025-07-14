# Update Menu Script

Script `updatemenu.sh` cung cấp một menu quản lý cập nhật thông qua Rofi với các tùy chọn sau:

## Tính năng

### 🔍 **Check Updates**
- Hiển thị danh sách các gói cần cập nhật
- Đếm số lượng gói có sẵn để cập nhật
- Sử dụng `checkupdates` để kiểm tra an toàn

### 🔄 **Update System**
- Cập nhật toàn bộ hệ thống với `pacman -Syu`
- Chạy trong terminal riêng để theo dõi tiến trình

### 📦 **Update AUR**
- Tự động phát hiện và sử dụng `yay` hoặc `paru`
- Cập nhật các gói từ AUR
- Hiển thị thông báo nếu không tìm thấy AUR helper

### 🔄 **Refresh Mirrors**
- Làm mới danh sách mirrors với `pacman -Syy`
- Đảm bảo kết nối đến mirrors mới nhất

### 🧹 **Clean Cache**
- Dọn dẹp cache gói với `pacman -Sc`
- Tiết kiệm dung lượng ổ cứng

### 📋 **View Logs**
- Xem 50 dòng cuối của log pacman
- Theo dõi các hoạt động cài đặt/gỡ bỏ gần đây

## Cách sử dụng

### Phím tắt
- Nhấn `Mod + c, u` để mở menu cập nhật

### Giao diện
- Menu sử dụng theme `modern-green.rasi` nhất quán với Qtile
- Hiển thị số lượng cập nhật có sẵn trong tiêu đề
- Các tùy chọn có icon trực quan

## Yêu cầu

- `pacman-contrib` (cho lệnh `checkupdates`)
- `yay` hoặc `paru` (tùy chọn, cho AUR)
- `rofi` với theme `modern-green.rasi`
- `wezterm` terminal

## Tùy chỉnh

Để thay đổi AUR helper hoặc terminal, chỉnh sửa file script tại:
```
~/.config/qtile/scripts/updatemenu.sh
```
