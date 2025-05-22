#!/bin/fish

# Debug: ghi log khi script được chạy
echo "ibus.sh script started at $(date)" >> /tmp/qtile_ibus_debug.log

# Kiểm tra xem ibus-daemon đã chạy chưa
if not pgrep -x "ibus-daemon" > /dev/null
    # Debug: ghi log khi khởi động ibus-daemon
    echo "Starting ibus-daemon (not running)" >> /tmp/qtile_ibus_debug.log

    # Nếu chưa chạy, khởi động ibus-daemon với cờ xim và tray icon
    # Sử dụng đường dẫn tuyệt đối để đảm bảo panel được tìm thấy
    set panel_path (find /usr/lib -name "ibus-ui-gtk3" 2>/dev/null | head -n 1)

    if test -n "$panel_path"
        echo "Found panel at: $panel_path" >> /tmp/qtile_ibus_debug.log
        ibus-daemon -drx --panel=$panel_path
    else
        echo "Panel not found, trying default path" >> /tmp/qtile_ibus_debug.log
        ibus-daemon -drx --panel=/usr/lib/ibus/ibus-ui-gtk3
    end

    # Debug: kiểm tra kết quả
    if pgrep -x "ibus-daemon" > /dev/null
        echo "ibus-daemon started successfully" >> /tmp/qtile_ibus_debug.log
    else
        echo "Failed to start ibus-daemon" >> /tmp/qtile_ibus_debug.log
    end
else
    # Debug: ghi log khi khởi động lại ibus-daemon
    echo "Restarting ibus-daemon (already running)" >> /tmp/qtile_ibus_debug.log

    # Nếu đã chạy, khởi động lại để đảm bảo tray icon hiển thị
    ibus-daemon -rdx
    sleep 1

    # Sử dụng đường dẫn tuyệt đối để đảm bảo panel được tìm thấy
    set panel_path (find /usr/lib -name "ibus-ui-gtk3" 2>/dev/null | head -n 1)

    if test -n "$panel_path"
        echo "Found panel at: $panel_path" >> /tmp/qtile_ibus_debug.log
        ibus-daemon -drx --panel=$panel_path
    else
        echo "Panel not found, trying default path" >> /tmp/qtile_ibus_debug.log
        ibus-daemon -drx --panel=/usr/lib/ibus/ibus-ui-gtk3
    end

    # Debug: kiểm tra kết quả
    if pgrep -x "ibus-daemon" > /dev/null
        echo "ibus-daemon restarted successfully" >> /tmp/qtile_ibus_debug.log
    else
        echo "Failed to restart ibus-daemon" >> /tmp/qtile_ibus_debug.log
    end
end

# Debug: kiểm tra các engine có sẵn
echo "Available ibus engines: $(ibus list-engine | grep name: | head -n 5)" >> /tmp/qtile_ibus_debug.log

# Đảm bảo ibus-bamboo được thiết lập là engine mặc định (nếu đã cài đặt)
if type -q ibus-setup
    # Debug: ghi log trước khi thiết lập engine
    echo "Setting Bamboo as default engine" >> /tmp/qtile_ibus_debug.log

    # Thiết lập engine
    ibus engine Bamboo 2>> /tmp/qtile_ibus_debug.log || echo "Failed to set Bamboo engine" >> /tmp/qtile_ibus_debug.log
end

# Debug: ghi log khi script kết thúc
echo "ibus.sh script completed at $(date)" >> /tmp/qtile_ibus_debug.log
