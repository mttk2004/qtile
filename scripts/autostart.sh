#!/bin/fish

# Lấy các biến môi trường từ settings.py
eval (python3 ~/.config/qtile/scripts/export_settings.py fish)

# Khởi động picom trước tiên để tránh độ trễ hiển thị
echo "Killing any existing picom instances..." > /tmp/picom_debug.log
killall -q picom 2>/dev/null || true

# Khởi động picom ngay lập tức với đường dẫn tuyệt đối và các tùy chọn cần thiết
set PICOM_CONFIG_PATH ~/.config/qtile/scripts/picom.conf
echo "Starting picom with config: $PICOM_CONFIG_PATH" >> /tmp/picom_debug.log
/sbin/picom --daemon --config $PICOM_CONFIG_PATH --corner-radius 13 >> /tmp/picom_debug.log 2>&1

# Khởi động các ứng dụng nền
feh --bg-fill $QTILE_DEFAULT_WALLPAPER &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Khởi động Wired với cấu hình mới
killall -q wired 2>/dev/null || true
sleep 0.5
/usr/bin/wired &

eval (gnome-keyring-daemon --start)

# Khởi động ibus-daemon
fish ~/.config/qtile/scripts/ibus.sh &

# Khởi động các ứng dụng không quan trọng sau
nm-applet &

# Kiểm tra thời gian và chạy redshift nếu cần
if test -n "$QTILE_REDSHIFT_SCRIPT"
    $QTILE_REDSHIFT_SCRIPT &
end

