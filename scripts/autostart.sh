#!/bin/fish

# Lấy các biến môi trường từ settings.py
eval (python3 ~/.config/qtile/scripts/export_settings.py fish)

# Khởi động các ứng dụng nền
feh --bg-fill $QTILE_DEFAULT_WALLPAPER &
picom --daemon --config $QTILE_PICOM_CONFIG &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/wired &
eval (gnome-keyring-daemon --start)
nm-applet &

# Khởi động ibus-daemon
$QTILE_IBUS_SCRIPT &

# Kiểm tra thời gian và chạy redshift nếu cần
$QTILE_REDSHIFT_SCRIPT &

