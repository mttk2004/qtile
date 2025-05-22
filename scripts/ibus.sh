#!/bin/fish

# Kiểm tra xem ibus-daemon đã chạy chưa
if not pgrep -x "ibus-daemon" > /dev/null
    # Nếu chưa chạy, khởi động ibus-daemon với cờ xim và tray icon
    # Sử dụng đường dẫn tuyệt đối để đảm bảo panel được tìm thấy
    set panel_path (find /usr/lib -name "ibus-ui-gtk3" 2>/dev/null | head -n 1)

    if test -n "$panel_path"
        ibus-daemon -drx --panel=$panel_path
    else
        ibus-daemon -drx --panel=/usr/lib/ibus/ibus-ui-gtk3
    end
else
    # Nếu đã chạy, khởi động lại để đảm bảo tray icon hiển thị
    ibus-daemon -rdx
    sleep 1

    # Sử dụng đường dẫn tuyệt đối để đảm bảo panel được tìm thấy
    set panel_path (find /usr/lib -name "ibus-ui-gtk3" 2>/dev/null | head -n 1)

    if test -n "$panel_path"
        ibus-daemon -drx --panel=$panel_path
    else
        ibus-daemon -drx --panel=/usr/lib/ibus/ibus-ui-gtk3
    end
end

# Đảm bảo ibus-bamboo được thiết lập là engine mặc định (nếu đã cài đặt)
if type -q ibus-setup
    ibus engine Bamboo 2>/dev/null || true
end
