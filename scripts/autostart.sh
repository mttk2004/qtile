#!/bin/fish

# Lấy các biến môi trường từ settings.py
eval (python3 ~/.config/qtile/scripts/export_settings.py fish)

# Khởi động các ứng dụng nền
feh --bg-fill $QTILE_DEFAULT_WALLPAPER &

# Đảm bảo picom được khởi động đúng cách
killall picom 2>/dev/null || true
sleep 1
picom --daemon --config $QTILE_PICOM_CONFIG &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/wired &
eval (gnome-keyring-daemon --start)
nm-applet &

# Khởi động ibus-daemon
fish ~/.config/qtile/scripts/ibus.sh &

# Kiểm tra thời gian và chạy redshift nếu cần
$QTILE_REDSHIFT_SCRIPT &

