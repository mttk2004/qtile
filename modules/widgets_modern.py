"""
Widget hiện đại cho Qtile.

Cung cấp các widget với thiết kế hiện đại, tối giản và thống nhất.
Sử dụng bảng màu từ themes/colors.py.
"""

from libqtile import widget, qtile
import subprocess
import os

from themes.colors import colors
from modules.settings import font_family, terminal, app_launcher, scripts_dir, icons_dir

# Đường dẫn đến thư mục icons
ICONS_DIR = os.path.expanduser(icons_dir)

# Điều chỉnh kích thước font
FONT_SIZE = 16  # Tăng kích thước font
ICON_SIZE = 22  # Tăng kích thước icon

# Utility functions
def open_launcher():
    """Mở app launcher."""
    qtile.cmd_spawn(app_launcher)

def open_terminal():
    """Mở terminal."""
    qtile.cmd_spawn(terminal)

def open_btop():
    """Mở btop trong terminal."""
    qtile.cmd_spawn(f"{terminal} --hold -e btop")

def open_powermenu():
    """Mở power menu."""
    qtile.cmd_spawn(f"{scripts_dir}powermenu.sh")

def open_screenshot_menu():
    """Mở menu chụp màn hình."""
    qtile.cmd_spawn(f"{scripts_dir}ksnipmenu.sh")

def init_widgets_defaults():
    """Khởi tạo các giá trị mặc định cho widgets."""
    return dict(
        font=font_family,
        fontsize=FONT_SIZE,
        padding=10,  # Tăng padding
        background=colors["bg"],
        foreground=colors["fg"],
    )

def init_widgets_list():
    """Khởi tạo danh sách widgets cho bar."""
    widgets_list = [
        # Logo/Menu button
        widget.TextBox(
            text=" ",  # Icon cho menu (nếu có font awesome)
            foreground=colors["green_accent"],
            fontsize=ICON_SIZE,
            padding=12,
            mouse_callbacks={'Button1': open_launcher},
        ),

        # Separator
        widget.Sep(
            linewidth=0,
            padding=12,
        ),

        # Group Box - Hiển thị các workspace
        widget.GroupBox(
            font=font_family,
            fontsize=18,  # Tăng kích thước font cho GroupBox
            margin_y=4,
            margin_x=5,
            padding_y=6,
            padding_x=5,
            borderwidth=3,
            active=colors["active"],
            inactive=colors["inactive_group"],
            rounded=True,
            highlight_color=colors["bg"],
            highlight_method="line",
            this_current_screen_border=colors["green_accent"],
            this_screen_border=colors["green_secondary"],
            other_current_screen_border=colors["green_dark"],
            other_screen_border=colors["inactive"],
            urgent_border=colors["error"],
            urgent_text=colors["error"],
            disable_drag=True,
        ),

        # Separator
        widget.Sep(
            linewidth=0,
            padding=12,
        ),

        # Current Layout Icon
        widget.CurrentLayoutIcon(
            scale=0.7,  # Tăng kích thước icon
            padding=0,
        ),

        # Current Layout
        widget.CurrentLayout(
            padding=8,
            foreground=colors["green_light"],
            fontsize=FONT_SIZE,
        ),

        # Separator
        widget.Sep(
            linewidth=1,
            padding=12,
            foreground=colors["inactive"],
        ),

        # Window Name
        widget.WindowName(
            format="{name}",
            max_chars=50,
            empty_group_string="Desktop",
            foreground=colors["fg"],
            padding=12,
            fontsize=FONT_SIZE,
        ),

        # Systray
        widget.Systray(
            icon_size=22,  # Tăng kích thước icon
            padding=12,
        ),

        # Separator
        widget.Sep(
            linewidth=0,
            padding=12,
        ),

        # CPU Widget với icon
        widget.TextBox(
            text="󰘚",  # Icon CPU (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=2,
        ),
        widget.CPU(
            format="{load_percent:.0f}%",
            foreground=colors["fg"],
            padding=8,
            update_interval=2.0,
            mouse_callbacks={'Button1': open_btop},
            fontsize=FONT_SIZE,
        ),

        # Memory Widget với icon
        widget.TextBox(
            text="󰍛",  # Icon RAM (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=12,
        ),
        widget.Memory(
            format="{MemUsed:.0f}MB",
            foreground=colors["fg"],
            padding=8,
            update_interval=2.0,
            mouse_callbacks={'Button1': open_btop},
            fontsize=FONT_SIZE,
        ),

        # Battery Widget với icon
        widget.TextBox(
            text="󰁹",  # Icon Pin (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=12,
        ),
        widget.Battery(
            format="{percent:2.0%}",
            foreground=colors["fg"],
            padding=8,
            update_interval=30,
            charge_char="󰂄",
            discharge_char="󰂃",
            full_char="󰁹",
            empty_char="󰂎",
            show_short_text=False,
            low_foreground=colors["warning"],
            low_percentage=0.15,
            fontsize=FONT_SIZE,
        ),

        # Volume Widget với icon
        widget.TextBox(
            text="󰕾",  # Icon Volume (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=12,
        ),
        widget.PulseVolume(
            foreground=colors["fg"],
            padding=8,
            limit_max_volume=True,
            fontsize=FONT_SIZE,
        ),

        # Brightness Widget với icon
        widget.TextBox(
            text="󰃠",  # Icon Brightness (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=12,
        ),
        widget.Backlight(
            backlight_name="amdgpu_bl0",
            format="{percent:2.0%}",
            foreground=colors["fg"],
            padding=8,
            change_command="brightnessctl s {0}%",
            step=5,
            fontsize=FONT_SIZE,
        ),

        # Separator
        widget.Sep(
            linewidth=1,
            padding=12,
            foreground=colors["inactive"],
        ),

        # Date Widget với icon
        widget.TextBox(
            text="󰸗",  # Icon Calendar (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=12,
        ),
        widget.Clock(
            format="%d/%m/%y",
            foreground=colors["fg"],
            padding=8,
            fontsize=FONT_SIZE,
        ),

        # Time Widget với icon
        widget.TextBox(
            text="󰥔",  # Icon Clock (nếu có font awesome)
            foreground=colors["green_primary"],
            fontsize=ICON_SIZE,
            padding=12,
        ),
        widget.Clock(
            format="%H:%M",
            foreground=colors["fg"],
            padding=8,
            fontsize=FONT_SIZE,
        ),

        # Separator
        widget.Sep(
            linewidth=0,
            padding=12,
        ),

        # Power Menu Button
        widget.TextBox(
            text="⏻",  # Icon Power (nếu có font awesome)
            foreground=colors["error"],
            fontsize=ICON_SIZE,
            padding=12,
            mouse_callbacks={'Button1': open_powermenu},
        ),
    ]
    return widgets_list

def init_secondary_widgets_list():
    """Khởi tạo danh sách widgets cho màn hình thứ hai."""
    # Đơn giản hóa widgets cho màn hình thứ hai
    widgets_list = init_widgets_list()
    # Loại bỏ systray vì chỉ nên hiển thị trên một màn hình
    for widget in widgets_list:
        if isinstance(widget, widget.Systray):
            widgets_list.remove(widget)
    return widgets_list
