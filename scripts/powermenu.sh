#!/bin/bash

# Power menu sử dụng Rofi với theme rounded-green-dark phù hợp với cấu hình hiện tại của Qtile

# Lựa chọn menu
options=("  Lock" "  Logout" "  Reboot" "  Shutdown" "  Suspend")

# Tạo menu với rofi
selected=$(printf "%s\n" "${options[@]}" | rofi -theme rounded-green-dark -dmenu -i -p "Power Menu")

# Thực hiện hành động tương ứng
case "$selected" in
    "  Lock")
        i3lock -c 000000
        ;;
    "  Logout")
        qtile cmd-obj -o cmd -f shutdown
        ;;
    "  Reboot")
        systemctl reboot
        ;;
    "  Shutdown")
        systemctl poweroff
        ;;
    "  Suspend")
        systemctl suspend
        ;;
    *)
        # Nếu không chọn gì
        echo "Không có hành động nào được chọn"
        ;;
esac
