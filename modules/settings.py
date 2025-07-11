"""
Cài đặt chung cho Qtile.

File này chứa tất cả các biến cấu hình được sử dụng trong toàn bộ dự án,
giúp tập trung quản lý và dễ dàng thay đổi khi cần.
"""

from typing import List, Dict, Any, Union
from types import FunctionType
from libqtile.core.manager import Qtile

# -----------------------------------------------------
# SYSTEM SETTINGS - Cài đặt hệ thống
# -----------------------------------------------------
MOD = "mod4"  # Windows key
MOD_ALT = "mod1"  # Alt key
TERMINAL = "wezterm"
FILEMANAGER = "thunar"
APP_LAUNCHER = "rofi -theme ~/.config/qtile/themes/rofi/modern-green-launcher.rasi -show drun -show-icons"
BROWSER = "firefox"
EDITOR = "code"
MUSIC_PLAYER = "spotify"
GPU_SCREEN_RECORDER = "flatpak run com.dec05eba.gpu_screen_recorder"

# -----------------------------------------------------
# APPEARANCE - Cài đặt giao diện
# -----------------------------------------------------
# Font settings
FONT_FAMILY = "CaskaydiaCove Nerd Font Regular"
FONT_SIZE = 18  # Kích thước font chính
ICON_SIZE = 32  # Kích thước icon
ICON_SIZE_SMALL = 28  # Kích thước icon nhỏ
DEFAULT_FONT = "sans"
DEFAULT_FONTSIZE = 16

# Bar settings
BAR_HEIGHT = 44  # Chiều cao thanh bar
BAR_MARGIN = [5, 8, 0, 8]  # [Top, Right, Bottom, Left]
SYSTRAY_ICON_SIZE = 24

# Widget settings
WIDGET_PADDING = 8  # Padding cho các widget
WIDGET_PADDING_SMALL = 4  # Padding nhỏ hơn cho một số widget
WIDGET_PADDING_LARGE = 20  # Padding lớn hơn cho một số widget
WIDGET_GROUPBOX_FONTSIZE = 20  # Kích thước font cho GroupBox
WIDGET_SEPARATOR_LINEWIDTH = 1  # Độ rộng của đường phân cách
WIDGET_UPDATE_INTERVAL = 5.0  # Tần suất cập nhật widget (giây)
WIDGET_BATTERY_UPDATE_INTERVAL = 30  # Tần suất cập nhật pin (giây)
WIDGET_MAX_CHARS = 50  # Số ký tự tối đa cho WindowName

# Layout settings
LAYOUT_MARGIN = 12  # Khoảng cách giữa các cửa sổ
LAYOUT_BORDER_WIDTH = 2  # Độ rộng viền cửa sổ
LAYOUT_RATIO = 0.6  # Tỷ lệ cửa sổ chính trong MonadTall/MonadWide
LAYOUT_MIN_RATIO = 0.30  # Tỷ lệ tối thiểu
LAYOUT_MAX_RATIO = 0.70  # Tỷ lệ tối đa
LAYOUT_CHANGE_RATIO = 0.05  # Bước thay đổi tỷ lệ
LAYOUT_GROW_AMOUNT = 2  # Lượng tăng kích thước cửa sổ

# TreeTab layout settings
TREETAB_FONTSIZE = 14
TREETAB_SECTION_FONTSIZE = 14
TREETAB_PADDING = 8
TREETAB_PANEL_WIDTH = 220
TREETAB_SECTION_TOP = 15

# Group settings
GROUP_LABELS = ["", "", "", "", "", "", "", "", ""]  # Nhãn cho các nhóm

# -----------------------------------------------------
# PATHS - Đường dẫn
# -----------------------------------------------------
# Assets paths
ASSETS_DIR = "~/.config/qtile/Assets/"
ICONS_DIR = f"{ASSETS_DIR}Bar-Icons/"
WALLPAPERS_DIR = "~/.config/qtile/Wallpaper/"
DEFAULT_WALLPAPER = f"{WALLPAPERS_DIR}bird.jpg"

# Scripts paths
SCRIPTS_DIR = "~/.config/qtile/scripts/"
POWERMENU_SCRIPT = f"{SCRIPTS_DIR}powermenu.sh"
KSNIPMENU_SCRIPT = f"{SCRIPTS_DIR}ksnipmenu.sh"
AUTOSTART_SCRIPT = f"{SCRIPTS_DIR}autostart.sh"
REDSHIFT_SCRIPT = f"{SCRIPTS_DIR}redshift.sh"
IBUS_SCRIPT = f"{SCRIPTS_DIR}ibus.sh"
TOGGLE_CONFIG_SCRIPT = f"{SCRIPTS_DIR}toggle_config.sh"
PICOM_CONFIG = f"{SCRIPTS_DIR}picom.conf"

# -----------------------------------------------------
# MISC - Cài đặt khác
# -----------------------------------------------------
# Window manager settings
FOLLOW_MOUSE_FOCUS = True
BRING_FRONT_CLICK = True
CURSOR_WARP = False  # This puts your mouse in the center on the screen after you switch to another workspace
AUTO_FULLSCREEN = True
FOCUS_ON_WINDOW_ACTIVATION = "smart"  # or focus
RECONFIGURE_SCREENS = True
AUTO_MINIMIZE = True
WM_NAME = "LG3D"

# Redshift settings
REDSHIFT_TEMP_NIGHT = 4500  # Nhiệt độ màu ban đêm (Kelvin)
REDSHIFT_TEMP_DAY = 6500  # Nhiệt độ màu ban ngày (Kelvin)

# Sticky window settings
STICKY_WINDOWS: List[Any] = []  # Danh sách cửa sổ sticky




