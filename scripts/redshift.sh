#!/bin/bash

# Đọc nhiệt độ màu từ file cấu hình
CONFIG_FILE="$HOME/.config/qtile/modules/settings.py"
TEMP_NIGHT=4500 # Giá trị mặc định

if [ -f "$CONFIG_FILE" ]; then
    # Lấy giá trị từ file cấu hình
    TEMP_VALUE=$(grep "redshift_temp_night" "$CONFIG_FILE" | grep -o '[0-9]\+')
    if [ ! -z "$TEMP_VALUE" ]; then
        TEMP_NIGHT=$TEMP_VALUE
    fi
fi

# Lấy giờ hiện tại (định dạng 24 giờ)
CURRENT_HOUR=$(date +%H)

# Kiểm tra xem có phải ban đêm không (từ 18:00 tối đến 6:00 sáng)
if [ "$CURRENT_HOUR" -ge 18 ] || [ "$CURRENT_HOUR" -lt 6 ]; then
    # Kiểm tra xem redshift đã chạy chưa
    if ! pgrep -x "redshift" > /dev/null; then
        # Nếu chưa chạy, khởi động redshift với nhiệt độ màu cấu hình
        redshift -O ${TEMP_NIGHT}K &
    else
        # Nếu đã chạy, thiết lập lại nhiệt độ màu
        redshift -O ${TEMP_NIGHT}K &
    fi
else
    # Ban ngày, thiết lập lại nhiệt độ màu mặc định (6500K)
    if pgrep -x "redshift" > /dev/null; then
        redshift -x
    fi
fi
