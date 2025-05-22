#!/bin/fish

# Debug: ghi log khi script autostart được chạy
echo "Autostart script started at $(date)" >> /tmp/qtile_autostart_debug.log

# Lấy các biến môi trường từ settings.py
eval (python3 ~/.config/qtile/scripts/export_settings.py fish)

# Debug: ghi log các biến môi trường
echo "QTILE_IBUS_SCRIPT = $QTILE_IBUS_SCRIPT" >> /tmp/qtile_autostart_debug.log

# Khởi động các ứng dụng nền
feh --bg-fill $QTILE_DEFAULT_WALLPAPER &
picom --daemon --config $QTILE_PICOM_CONFIG &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/wired &
eval (gnome-keyring-daemon --start)
nm-applet &

# Khởi động ibus-daemon
echo "Starting ibus-daemon using direct path" >> /tmp/qtile_autostart_debug.log
# Sử dụng đường dẫn tuyệt đối thay vì biến môi trường
fish ~/.config/qtile/scripts/ibus.sh >> /tmp/qtile_autostart_debug.log 2>&1 &

# Kiểm tra thời gian và chạy redshift nếu cần
$QTILE_REDSHIFT_SCRIPT &

