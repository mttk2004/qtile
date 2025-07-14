#!/bin/fish

# Lấy các biến môi trường từ settings.py
eval (python3 ~/.config/qtile/scripts/export_settings.py fish)

# Update menu sử dụng Rofi với theme modern-green phù hợp với cấu hình hiện tại của Qtile

# Kiểm tra số lượng gói cần cập nhật
set update_count (checkupdates 2>/dev/null | wc -l)

# Lựa chọn menu
if test $update_count -gt 0
    set options "  Check Updates ($update_count available)" "  Update System" "  Update AUR" "  Refresh Mirrors" "  Clean Cache" "  View Logs"
else
    set options "  Check Updates (System up to date)" "  Update System" "  Update AUR" "  Refresh Mirrors" "  Clean Cache" "  View Logs"
end

# Tạo menu với rofi
set selected (printf "%s\n" $options | rofi -theme ~/.config/qtile/themes/rofi/modern-green.rasi -dmenu -i -p "Update Manager")

# Thực hiện hành động tương ứng
switch "$selected"
    case "  Check Updates*"
        # Hiển thị danh sách cập nhật trong terminal
        wezterm --hold -e fish -c "
            echo '=== Checking for updates ===';
            checkupdates;
            echo '';
            echo 'Press any key to continue...';
            read -n 1
        "
    case "  Update System"
        # Cập nhật hệ thống
        wezterm --hold -e fish -c "
            echo '=== Updating system packages ===';
            sudo pacman -Syu;
            echo '';
            echo 'Press any key to continue...';
            read -n 1
        "
    case "  Update AUR"
        # Cập nhật AUR packages (nếu có yay hoặc paru)
        if command -v yay >/dev/null 2>&1
            wezterm --hold -e fish -c "
                echo '=== Updating AUR packages with yay ===';
                yay -Sua;
                echo '';
                echo 'Press any key to continue...';
                read -n 1
            "
        else if command -v paru >/dev/null 2>&1
            wezterm --hold -e fish -c "
                echo '=== Updating AUR packages with paru ===';
                paru -Sua;
                echo '';
                echo 'Press any key to continue...';
                read -n 1
            "
        else
            notify-send "Update Manager" "No AUR helper found (yay or paru required)"
        end
    case "  Refresh Mirrors"
        # Làm mới mirrors
        wezterm --hold -e fish -c "
            echo '=== Refreshing package mirrors ===';
            sudo pacman -Syy;
            echo '';
            echo 'Press any key to continue...';
            read -n 1
        "
    case "  Clean Cache"
        # Dọn dẹp cache
        wezterm --hold -e fish -c "
            echo '=== Cleaning package cache ===';
            sudo pacman -Sc;
            echo '';
            echo 'Press any key to continue...';
            read -n 1
        "
    case "  View Logs"
        # Xem log pacman
        wezterm --hold -e fish -c "
            echo '=== Recent pacman logs ===';
            tail -50 /var/log/pacman.log;
            echo '';
            echo 'Press any key to continue...';
            read -n 1
        "
    case "*"
        # Nếu không chọn gì
        echo "No action was chosen"
end
