#!/bin/fish

# Khởi động picom với cấu hình từ file picom.conf
picom --daemon --config $HOME/.config/qtile/scripts/picom.conf &

# Khởi động polkit-gnome-authentication-agent-1
(sleep 3 && /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1) &

# Khởi động wired
(sleep 2 && /usr/bin/wired) &

# Khởi động gnome-keyring-daemon
eval (gnome-keyring-daemon --start)

# Khởi động nm-applet
(sleep 2 && nm-applet) &

# Khởi động ibus-daemon
$HOME/.config/qtile/scripts/ibus.sh &

# Khởi động redshift
$HOME/.config/qtile/scripts/redshift.sh &
