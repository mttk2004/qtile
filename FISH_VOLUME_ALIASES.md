# Fish Shell Volume Aliases - PipeWire/PulseAudio

## Tổng quan
Các alias này được thiết kế để quản lý âm lượng thông qua `pactl` (PulseAudio/PipeWire control), thay thế cho `amixer` để tương thích tốt hơn với PipeWire.

## Điều khiển âm lượng cơ bản

### Tăng/Giảm âm lượng
```bash
volup      # Tăng âm lượng 5%
voldown    # Giảm âm lượng 5%
volmute    # Bật/tắt tiếng (toggle mute)
```

### Đặt âm lượng theo mức cố định
```bash
volzero      # 0%
volten       # 10%
voltwenty    # 20%
volthirty    # 30%
volforty     # 40%
volfifty     # 50%
volsixty     # 60%
volseventy   # 70%
voleighty    # 80%
volninety    # 90%
volhundred   # 100%
```

### Đặt âm lượng tùy chỉnh
```bash
volcustom 75%    # Đặt âm lượng 75%
volcustom 25%    # Đặt âm lượng 25%
```

## Kiểm tra trạng thái âm thanh

### Xem thông tin chi tiết
```bash
volinfo      # Hiển thị âm lượng hiện tại (left/right channels)
volstatus    # Kiểm tra trạng thái mute (yes/no)
vollist      # Liệt kê tất cả thiết bị âm thanh có sẵn
```

### Sửa chữa sự cố
```bash
volrestart   # Khởi động lại PulseAudio/PipeWire service
```

## Ví dụ sử dụng

```bash
# Kiểm tra âm lượng hiện tại
=> volinfo
Volume: front-left: 32768 /  50% / -18.06 dB,   front-right: 32768 /  50% / -18.06 dB

# Tăng âm lượng
=> volup

# Đặt âm lượng về 75%
=> volcustom 75%

# Tắt tiếng
=> volmute

# Kiểm tra trạng thái mute
=> volstatus
Mute: yes
```

## Tương thích

- ✅ **PipeWire** - Hoạt động hoàn hảo (khuyến nghị)
- ✅ **PulseAudio** - Hoạt động tốt
- ❌ **ALSA only** - Không tương thích (cần cài PulseAudio hoặc PipeWire)

## Lưu ý

- Tất cả lệnh sử dụng `@DEFAULT_SINK@` để tự động chọn thiết bị âm thanh mặc định
- Aliases này đồng bộ với cấu hình âm lượng trong Qtile
- Phím tắt trong Qtile (XF86Audio*) cũng sử dụng `pactl` để đảm bảo nhất quán
