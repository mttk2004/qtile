#!/bin/bash

# Script để chuyển đổi giữa cấu hình Qtile cũ và mới
# Sử dụng: ./toggle_config.sh

CONFIG_DIR="$HOME/.config/qtile"
CURRENT_CONFIG_SYMLINK="$CONFIG_DIR/config.py"
MODERN_CONFIG="$CONFIG_DIR/config_modern.py"
CLASSIC_CONFIG="$CONFIG_DIR/config_classic.py"

# Kiểm tra xem đã có bản sao lưu config_classic.py chưa
# Nếu config.py hiện tại không phải là symlink và không phải config_modern,
# thì coi nó là config_classic và tạo bản sao lưu.
if [ ! -L "$CURRENT_CONFIG_SYMLINK" ] && [ "$(basename "$(readlink -f "$CURRENT_CONFIG_SYMLINK")")" != "config_modern.py" ]; then
    echo "Tạo bản sao lưu cấu hình cũ thành config_classic.py..."
    cp "$CURRENT_CONFIG_SYMLINK" "$CLASSIC_CONFIG"
fi

# Kiểm tra cấu hình hiện tại là gì (dựa vào symlink)
if [ -L "$CURRENT_CONFIG_SYMLINK" ] && [ "$(readlink "$CURRENT_CONFIG_SYMLINK")" = "$MODERN_CONFIG" ]; then
    echo "Đang sử dụng cấu hình hiện đại. Chuyển sang cấu hình cũ..."
    ln -sf "$CLASSIC_CONFIG" "$CURRENT_CONFIG_SYMLINK"
    echo "Đã chuyển sang cấu hình cũ."
else
    echo "Đang sử dụng cấu hình cũ hoặc không xác định. Chuyển sang cấu hình hiện đại..."
    ln -sf "$MODERN_CONFIG" "$CURRENT_CONFIG_SYMLINK"
    echo "Đã chuyển sang cấu hình hiện đại."
fi

echo "Bạn có thể khởi động lại Qtile bằng cách nhấn Mod+Ctrl+R hoặc chạy 'qtile cmd-obj -o cmd -f restart'"