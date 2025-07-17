"""
Cấu hình màn hình hiện đại cho Qtile.

Sử dụng widgets hiện đại từ widgets_modern.py và cài đặt từ settings.py.
"""

from libqtile.config import Screen
from libqtile import bar
import os
import subprocess

from modules.settings import BAR_HEIGHT, BAR_MARGIN, DEFAULT_WALLPAPER
from modules.widgets_modern import init_widgets_list, init_secondary_widgets_list
from themes.colors import colors

def init_screens():
    """Khởi tạo danh sách màn hình.

    Hỗ trợ nhiều màn hình với cấu hình khác nhau.
    """
    # Cấu hình thanh bar hiện đại
    bar_config = {
        "size": BAR_HEIGHT,
        "background": colors["bg"],
        "margin": BAR_MARGIN,  # [Top, Right, Bottom, Left]
        "border_width": [0, 10, 0, 6],  # [Top, Right, Bottom, Left]
        "border_color": colors["bg"],  # Màu viền thanh bar
        "opacity": .9,  # Độ mờ của thanh bar
    }

    # Danh sách màn hình
    screens = [
        # Màn hình chính
        Screen(
            top=bar.Bar(
                init_widgets_list(),
                **bar_config,
            ),
            wallpaper=os.path.expanduser(DEFAULT_WALLPAPER),
            wallpaper_mode="fill",
        ),
    ]

    # Thêm màn hình thứ hai nếu có
    try:
        output = subprocess.check_output(["xrandr"]).decode("utf-8")
        num_screens = len([line for line in output.splitlines() if " connected " in line])
        if num_screens > 1:
            screens.append(
                Screen(
                    top=bar.Bar(
                        init_secondary_widgets_list(),
                        **bar_config,
                    ),
                    wallpaper=os.path.expanduser(DEFAULT_WALLPAPER),
                    wallpaper_mode="fill",
                )
            )
    except (FileNotFoundError, subprocess.CalledProcessError):
        # Bỏ qua nếu xrandr không tồn tại hoặc có lỗi
        pass

    return screens
