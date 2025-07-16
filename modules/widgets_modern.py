"""
Widget hiện đại cho Qtile.

Cung cấp các widget với thiết kế hiện đại, tối giản và thống nhất.
Sử dụng bảng màu từ themes/colors.py.
"""

from typing import List, Dict, Any, Callable, Optional, TYPE_CHECKING
from libqtile import widget, qtile
from libqtile.lazy import lazy
import subprocess
import os
import re
import logging

if TYPE_CHECKING:
    from libqtile.core.manager import Qtile

from themes.colors import colors
from modules.settings import (
    FONT_FAMILY, FONT_SIZE, ICON_SIZE, ICON_SIZE_SMALL, TERMINAL, APP_LAUNCHER, SCRIPTS_DIR, ICONS_DIR,
    WIDGET_PADDING, WIDGET_PADDING_SMALL, WIDGET_PADDING_LARGE, WIDGET_GROUPBOX_FONTSIZE, WIDGET_SEPARATOR_LINEWIDTH,
    WIDGET_UPDATE_INTERVAL, WIDGET_BATTERY_UPDATE_INTERVAL, WIDGET_MAX_CHARS, SYSTRAY_ICON_SIZE
)

# Configure logging
logger = logging.getLogger(__name__)

# Đường dẫn đến thư mục icons
ICONS_PATH = os.path.expanduser(ICONS_DIR)

# --- Utility functions ---
def open_launcher() -> None:
    """Mở app launcher."""
    lazy.spawn(APP_LAUNCHER)()

def open_terminal() -> None:
    """Mở terminal."""
    lazy.spawn(TERMINAL)()

def open_btop() -> None:
    """Mở btop trong terminal."""
    lazy.spawn(f"{TERMINAL} --hold -e btop")()

def open_powermenu() -> None:
    """Mở power menu."""
    try:
        script_path = os.path.expanduser(f"{SCRIPTS_DIR}powermenu.sh")
        subprocess.Popen([script_path])
    except FileNotFoundError:
        logger.error(f"Power menu script not found at {script_path}")
    except Exception as e:
        logger.error(f"Failed to open power menu: {e}")

def get_backlight_name() -> str:
    """Tự động tìm tên thiết bị backlight."""
    try:
        # Lấy danh sách các thiết bị backlight
        backlight_devices = os.listdir('/sys/class/backlight/')
        if backlight_devices:
            return backlight_devices[0]  # Trả về thiết bị đầu tiên tìm thấy
    except (FileNotFoundError, OSError) as e:
        logger.warning(f"Could not find backlight devices: {e}")
    return "amdgpu_bl0"  # Giá trị dự phòng

def get_volume_pipewire() -> str:
    """Lấy thông tin âm lượng từ PipeWire qua pactl."""
    try:
        # Lấy thông tin âm lượng
        volume_output = subprocess.check_output(
            ["pactl", "get-sink-volume", "@DEFAULT_SINK@"],
            text=True
        ).strip()

        # Parse volume từ output như "Volume: front-left: 32768 /  50% / -18.06 dB"
        volume_match = re.search(r'(\d+)%', volume_output)
        volume = volume_match.group(1) if volume_match else "0"

        # Kiểm tra trạng thái mute
        mute_output = subprocess.check_output(
            ["pactl", "get-sink-mute", "@DEFAULT_SINK@"],
            text=True
        ).strip()

        if "yes" in mute_output.lower():
            return "🔇 Muted"
        else:
            return f"{volume}%"

    except subprocess.CalledProcessError as e:
        logger.warning(f"Failed to get volume info: {e}")
        return "N/A"
    except Exception as e:
        logger.error(f"Unexpected error getting volume: {e}")
        return "Error"

# --- Widget Defaults ---
def init_widgets_defaults() -> Dict[str, Any]:
    """Khởi tạo các giá trị mặc định cho widgets."""
    return dict(
        font=FONT_FAMILY,
        fontsize=FONT_SIZE,
        padding=WIDGET_PADDING,
        background=colors["bg"],
        foreground=colors["fg"],
    )

# --- Helper functions for creating widget groups ---

def _init_groupbox_widgets() -> List[widget.GroupBox]:
    """Tạo widget GroupBox với cấu hình hiện đại."""
    return [
        widget.GroupBox(
            font=FONT_FAMILY,
            fontsize=WIDGET_GROUPBOX_FONTSIZE,
            margin_y=5,
            margin_x=2,
            padding_y=8,
            padding_x=5,
            borderwidth=3,
            active=colors["active"],
            inactive=colors["inactive_group"],
            rounded=True,
            highlight_color=colors["bg"],
            highlight_method="text",
            urgent_alert_method="text",
            this_current_screen_border=colors["green_accent"],
            this_screen_border=colors["green_secondary"],
            other_current_screen_border=colors["green_dark"],
            other_screen_border=colors["inactive"],
            urgent_border=colors["error"],
            urgent_text=colors["error"],
            disable_drag=True,
        ),
    ]

def _init_layout_widgets() -> List[widget.CurrentLayout]:
    """Tạo widget hiển thị layout hiện tại."""
    return [
        widget.CurrentLayout(
            font=FONT_FAMILY,
            padding=WIDGET_PADDING_SMALL,
            foreground=colors["green_light"],
            fontsize=FONT_SIZE,
        ),
    ]

def _init_window_name_widget() -> List[widget.WindowName]:
    """Tạo widget hiển thị tên cửa sổ hiện tại."""
    return [
        widget.WindowName(
            font=FONT_FAMILY,
            format="{name}",
            max_chars=WIDGET_MAX_CHARS,
            empty_group_string="Desktop",
            foreground=colors["fg"],
            padding=WIDGET_PADDING,
            fontsize=FONT_SIZE,
        ),
    ]

def _init_systray_widget() -> List[widget.Systray]:
    """Tạo widget system tray."""
    return [
        widget.Systray(
            icon_size=SYSTRAY_ICON_SIZE,
        ),
    ]

def _init_system_info_widgets() -> List[Any]:
    """Tạo các widget hiển thị thông tin hệ thống (CPU, RAM)."""
    return [
        widget.TextBox(
            text="󰘚",  # Icon CPU
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.CPU(
            font=FONT_FAMILY,
            format="{load_percent:.0f}%",
            foreground=colors["fg"],
            padding=WIDGET_PADDING_SMALL,
            update_interval=WIDGET_UPDATE_INTERVAL,
            mouse_callbacks={'Button1': open_btop},
            fontsize=FONT_SIZE,
        ),
        widget.TextBox(
            text=" 󰍛",  # Icon RAM
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=WIDGET_PADDING,
        ),
        widget.Memory(
            font=FONT_FAMILY,
            format="{MemUsed:.0f}MB",
            foreground=colors["fg"],
            update_interval=WIDGET_UPDATE_INTERVAL,
            mouse_callbacks={'Button1': open_btop},
            fontsize=FONT_SIZE,
        ),
    ]

def _init_device_status_widgets() -> List[Any]:
    """Tạo các widget hiển thị trạng thái thiết bị (pin, độ sáng, âm lượng)."""
    return [
        widget.TextBox(
            text=" 󰁹",  # Icon Pin
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE_SMALL,
            padding=WIDGET_PADDING,
        ),
        widget.Battery(
            font=FONT_FAMILY,
            format="{percent:2.0%}",
            foreground=colors["fg"],
            update_interval=WIDGET_BATTERY_UPDATE_INTERVAL,
            charge_char="󰂄",
            discharge_char="󰂃",
            full_char="󰁹",
            empty_char="󰂎",
            show_short_text=False,
            low_foreground=colors["warning"],
            low_percentage=0.15,
            fontsize=FONT_SIZE,
        ),
        widget.TextBox(
            text=" 󰕾",  # Icon Volume
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        # Widget Volume tùy chỉnh cho PipeWire
        # Click chuột trái: toggle mute
        # Scroll lên/xuống: tăng/giảm âm lượng
        widget.GenPollText(
            font=FONT_FAMILY,
            foreground=colors["fg"],
            fontsize=FONT_SIZE,
            func=lambda: get_volume_pipewire(),
            update_interval=1,
            mouse_callbacks={
                'Button1': lambda: lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")(),
                'Button4': lambda: lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")(),
                'Button5': lambda: lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")(),
            },
        ),
        widget.TextBox(
            text=" 󰃠",  # Icon Brightness
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.Backlight(
            backlight_name=get_backlight_name(),
            font=FONT_FAMILY,
            format="{percent:2.0%}",
            foreground=colors["fg"],
            change_command="brightnessctl s {0}%",
            step=5,
            fontsize=FONT_SIZE,
        ),
    ]

def _init_clock_widgets():
    return [
        widget.TextBox(
            text=" 󰸗",  # Icon Calendar
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.Clock(
            font=FONT_FAMILY,
            format="%d/%m/%y",
            foreground=colors["fg"],
            fontsize=FONT_SIZE,
        ),
        widget.TextBox(
            text=" 󰥔",  # Icon Clock
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
        ),
        widget.Clock(
            font=FONT_FAMILY,
            format="%H:%M",
            foreground=colors["fg"],
            fontsize=FONT_SIZE,
        ),
    ]

def _init_power_widget():
    return [
        widget.TextBox(
            text="⏻",  # Icon Power
            foreground=colors["error"],
            fontsize=ICON_SIZE,
            mouse_callbacks={'Button1': open_powermenu},
        ),
    ]

def _separator():
    return widget.Sep(
        linewidth=WIDGET_SEPARATOR_LINEWIDTH,
        padding=WIDGET_PADDING_LARGE,
        foreground=colors["inactive"],
    )

# --- Main Widget Lists ---

def init_widgets_list():
    """Khởi tạo danh sách widgets cho bar chính."""
    widgets_list = [
        *_init_groupbox_widgets(),
        _separator(),
        *_init_layout_widgets(),
        _separator(),
        *_init_window_name_widget(),
        _separator(),
        *_init_systray_widget(),
        _separator(),
        *_init_system_info_widgets(),
        *_init_device_status_widgets(),
        *_init_clock_widgets(),
        _separator(),
        *_init_power_widget(),
    ]
    return widgets_list

def init_secondary_widgets_list():
    """Khởi tạo danh sách widgets cho màn hình thứ hai."""
    # Bắt đầu với danh sách widget đầy đủ
    widgets_list = init_widgets_list()

    # Tạo một danh sách mới không có Systray
    secondary_widgets = [w for w in widgets_list if not isinstance(w, widget.Systray)]

    return secondary_widgets
