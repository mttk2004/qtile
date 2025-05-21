"""
Cấu hình màn hình hiện đại cho Qtile.

Sử dụng widgets hiện đại từ widgets_modern.py.
"""

from libqtile.config import Screen
from libqtile import bar
import os

from modules.settings import bar_height
from modules.widgets_modern import init_widgets_list, init_secondary_widgets_list
from themes.colors import colors

def init_screens():
    """Khởi tạo danh sách màn hình.

    Hỗ trợ nhiều màn hình với cấu hình khác nhau.
    """
    # Điều chỉnh kích thước thanh bar
    bar_size = 44  # Tăng kích thước thanh bar lên 44px để phù hợp với font lớn hơn

    # Cấu hình thanh bar hiện đại
    bar_config = {
        "size": bar_size,
        "background": colors["bg"],
        "margin": [5, 8, 0, 8],  # [Top, Right, Bottom, Left] - Tăng margin top
        "border_width": [0, 0, 0, 0],  # [Top, Right, Bottom, Left] - Tắt border
    }

    # Danh sách màn hình
    screens = [
        # Màn hình chính
        Screen(
            top=bar.Bar(
                init_widgets_list(),
                **bar_config,
            ),
            # Có thể thêm wallpaper nếu muốn
            # wallpaper="~/.config/qtile/wallpapers/wallpaper.jpg",
            # wallpaper_mode="fill",
        ),
    ]

    # Thêm màn hình thứ hai nếu có
    # Kiểm tra xem có màn hình thứ hai không bằng cách kiểm tra xrandr hoặc các file trong /sys/class/drm
    connected_displays = []
    try:
        # Kiểm tra các card màn hình đã kết nối
        for card in os.listdir("/sys/class/drm"):
            card_path = f"/sys/class/drm/{card}/status"
            if os.path.isfile(card_path):
                with open(card_path, "r") as f:
                    if f.read().strip() == "connected":
                        connected_displays.append(card)

        # Nếu có nhiều hơn 1 màn hình đã kết nối
        if len(connected_displays) > 1:
            screens.append(
                Screen(
                    top=bar.Bar(
                        init_secondary_widgets_list(),
                        **bar_config,
                    ),
                    # wallpaper="~/.config/qtile/wallpapers/wallpaper2.jpg",
                    # wallpaper_mode="fill",
                )
            )
    except (FileNotFoundError, IOError, OSError):
        # Nếu không thể kiểm tra, chỉ sử dụng một màn hình
        pass

    return screens
