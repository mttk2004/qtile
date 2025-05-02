#!/bin/bash

# Kiểm tra xem ibus-daemon đã chạy chưa
if ! pgrep -x "ibus-daemon" > /dev/null; then
    # Nếu chưa chạy, khởi động ibus-daemon
    ibus-daemon -drx
fi
