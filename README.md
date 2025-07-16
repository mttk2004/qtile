# Qtile Configuration

Cấu hình Qtile hiện đại với thiết kế tối giản và hiệu quả.

## Tính năng

- Thiết kế hiện đại với tông màu xanh lá chủ đạo
- Hỗ trợ nhiều màn hình tự động
- Widget hiện đại với các icon và thông tin hữu ích
- Layouts đa dạng và tùy biến cao
- Tối ưu hiệu suất và trải nghiệm người dùng

## Cấu trúc thư mục

```
qtile/
├── config.py              # File cấu hình chính đang sử dụng
├── modules/               # Thư mục chứa các module chức năng
│   ├── keys.py            # Cấu hình phím tắt
│   ├── groups.py          # Cấu hình nhóm cửa sổ
│   ├── layouts_modern.py  # Cấu hình bố cục cửa sổ
│   ├── screens_modern.py  # Cấu hình màn hình
│   ├── widgets_modern.py  # Cấu hình widget
│   ├── hooks.py           # Các hook và callback
│   ├── mouse.py           # Cấu hình chuột
│   └── settings.py        # Các cài đặt chung
├── themes/                # Thư mục chứa theme
│   ├── __init__.py        # Export theme
│   ├── colors.py          # Định nghĩa màu sắc
│   └── rofi/              # Theme rofi
├── scripts/               # Scripts tiện ích
│   ├── autostart.sh       # Script khởi động các ứng dụng
│   ├── powermenu.sh       # Script menu nguồn
│   ├── ksnipmenu.sh       # Script menu chụp màn hình
│   ├── redshift.sh        # Script điều chỉnh màu màn hình
│   ├── ibus.sh            # Script cấu hình bộ gõ
│   └── picom.conf         # Cấu hình picom
├── Assets/                # Thư mục chứa tài nguyên
│   └── Bar-Icons/         # Icons cho thanh bar
└── Wallpaper/             # Thư mục chứa hình nền
```

## Tùy chỉnh

### Thay đổi màu sắc

Chỉnh sửa file `themes/colors.py` để thay đổi bảng màu.

### Thay đổi widget

Chỉnh sửa file `modules/widgets_modern.py` để thay đổi các widget trên thanh bar.

### Thay đổi layout

Chỉnh sửa file `modules/layouts_modern.py` để thay đổi các layout cửa sổ.

## Phím tắt

| Phím tắt           | Mô tả                                     |
| :----------------- | :---------------------------------------- |
| `Mod + Enter`      | Mở terminal                               |
| `Mod + q`          | Đóng cửa sổ hiện tại                      |
| `Mod + Tab`        | Chuyển đổi cửa sổ với Rofi                |
| `Mod + Shift + Tab`| Chuyển đổi giữa các layout                |
| `Mod + [1-9]`      | Chuyển đổi giữa các workspace             |
| `Mod + Shift + [1-9]` | Di chuyển cửa sổ hiện tại đến workspace khác |
| `Mod + h/j/k/l`    | Di chuyển giữa các cửa sổ                 |
| `Mod + Shift + h/j/k/l` | Di chuyển cửa sổ                      |
| `Mod + Ctrl + h/j/k/l`  | Thay đổi kích thước cửa sổ            |
| `Mod + Shift + f`  | Bật/tắt chế độ nổi của cửa sổ             |
| `Mod + Shift + c`  | Căn giữa cửa sổ nổi                       |
| `Mod + f`          | Bật/tắt chế độ toàn màn hình              |
| `Mod + d`          | Mở trình khởi chạy ứng dụng (Rofi)        |
| `Mod + c, r`       | Khởi động lại Qtile                       |
| `Mod + c, q`       | Đăng xuất khỏi Qtile                      |
| `Mod + c, p`       | Mở menu nguồn                             |
| `Print`            | Chụp màn hình với Flameshot               |
| `Mod + Ctrl + p`   | Mở menu chụp màn hình (Ksnip)             |
| `Mod + e`          | Mở trình quản lý tệp (Thunar)             |
| `Mod + s`          | Bật/tắt chế độ sticky cho cửa sổ hiện tại |
| `Mod + g`          | Mở trình quay màn hình GPU                |
| `Mod + Alt + Left` | Chuyển đến workspace trước đó             |
| `Mod + Alt + Right`| Chuyển đến workspace tiếp theo            |
| `Mod + F10`        | Bật/tắt scratchpad monitor                |
| `Mod + F11`        | Bật/tắt scratchpad terminal               |
| `Mod + F12`        | Bật/tắt scratchpad file manager           |
| `XF86AudioRaiseVolume` | Tăng âm lượng                           |
| `XF86AudioLowerVolume` | Giảm âm lượng                           |
| `XF86AudioMute`    | Tắt/bật tiếng                             |
| `XF86AudioPlay`    | Phát/tạm dừng nhạc                        |
| `XF86AudioPrev`    | Bài hát trước                             |
| `XF86AudioNext`    | Bài hát tiếp theo                         |
| `XF86MonBrightnessUp` | Tăng độ sáng màn hình                    |
| `XF86MonBrightnessDown` | Giảm độ sáng màn hình                    |
| `XF86TouchpadToggle` | Bật/tắt touchpad                         |
