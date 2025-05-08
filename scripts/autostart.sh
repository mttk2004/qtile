#!/bin/fish

feh --bg-fill $HOME/.config/qtile/Wallpaper/Skyscraper.png &
picom --daemon --config $HOME/.config/qtile/scripts/picom.conf &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
/usr/bin/wired &
eval (gnome-keyring-daemon --start)
nm-applet &

# Khởi động ibus-daemon
$HOME/.config/qtile/scripts/ibus.sh &

# Kiểm tra thời gian và chạy redshift nếu cần
$HOME/.config/qtile/scripts/redshift.sh &

