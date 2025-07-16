"""
Cài đặt chung cho Qtile.

File này chứa tất cả các biến cấu hình được sử dụng trong toàn bộ dự án,
giúp tập trung quản lý và dễ dàng thay đổi khi cần.
"""

from typing import List, Dict, Any, Union, Final
import os

# -----------------------------------------------------
# SYSTEM SETTINGS - Cài đặt hệ thống
# -----------------------------------------------------
MOD: Final[str] = "mod4"  # Windows key
MOD_ALT: Final[str] = "mod1"  # Alt key
TERMINAL: Final[str] = "wezterm"
FILEMANAGER: Final[str] = "thunar"
BROWSER: Final[str] = "firefox"
EDITOR: Final[str] = "code"
MUSIC_PLAYER: Final[str] = "spotify"
GPU_SCREEN_RECORDER: Final[str] = "flatpak run com.dec05eba.gpu_screen_recorder"

# Rofi theme path
_ROFI_THEME_PATH: Final[str] = "~/.config/qtile/themes/rofi/modern-green-launcher.rasi"
APP_LAUNCHER: Final[str] = f"rofi -theme {_ROFI_THEME_PATH} -show drun -show-icons"

# -----------------------------------------------------
# APPEARANCE - Cài đặt giao diện
# -----------------------------------------------------
# Font settings
FONT_FAMILY: Final[str] = "CaskaydiaCove Nerd Font Regular"
FONT_SIZE: Final[int] = 18  # Kích thước font chính
ICON_SIZE: Final[int] = 32  # Kích thước icon
ICON_SIZE_SMALL: Final[int] = 28  # Kích thước icon nhỏ
DEFAULT_FONT: Final[str] = "sans"
DEFAULT_FONTSIZE: Final[int] = 16

# Bar settings
BAR_HEIGHT: Final[int] = 44  # Chiều cao thanh bar
BAR_MARGIN: Final[List[int]] = [5, 8, 0, 8]  # [Top, Right, Bottom, Left]
SYSTRAY_ICON_SIZE: Final[int] = 24

# Widget settings
WIDGET_PADDING: Final[int] = 8  # Padding cho các widget
WIDGET_PADDING_SMALL: Final[int] = 4  # Padding nhỏ hơn cho một số widget
WIDGET_PADDING_LARGE: Final[int] = 20  # Padding lớn hơn cho một số widget
WIDGET_GROUPBOX_FONTSIZE: Final[int] = 20  # Kích thước font cho GroupBox
WIDGET_SEPARATOR_LINEWIDTH: Final[int] = 1  # Độ rộng của đường phân cách
WIDGET_UPDATE_INTERVAL: Final[float] = 5.0  # Tần suất cập nhật widget (giây)
WIDGET_BATTERY_UPDATE_INTERVAL: Final[int] = 30  # Tần suất cập nhật pin (giây)
WIDGET_MAX_CHARS: Final[int] = 50  # Số ký tự tối đa cho WindowName

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
# Base directories
_CONFIG_DIR: Final[str] = "~/.config/qtile"
ASSETS_DIR: Final[str] = f"{_CONFIG_DIR}/Assets/"
WALLPAPERS_DIR: Final[str] = f"{_CONFIG_DIR}/Wallpaper/"
SCRIPTS_DIR: Final[str] = f"{_CONFIG_DIR}/scripts/"

# Specific paths
ICONS_DIR: Final[str] = f"{ASSETS_DIR}Bar-Icons/"
DEFAULT_WALLPAPER: Final[str] = f"{WALLPAPERS_DIR}bird.jpg"

# Script paths
POWERMENU_SCRIPT: Final[str] = f"{SCRIPTS_DIR}powermenu.sh"
KSNIPMENU_SCRIPT: Final[str] = f"{SCRIPTS_DIR}ksnipmenu.sh"
AUTOSTART_SCRIPT: Final[str] = f"{SCRIPTS_DIR}autostart.sh"
REDSHIFT_SCRIPT: Final[str] = f"{SCRIPTS_DIR}redshift.sh"
IBUS_SCRIPT: Final[str] = f"{SCRIPTS_DIR}ibus.sh"
PICOM_CONFIG: Final[str] = f"{SCRIPTS_DIR}picom.conf"

# -----------------------------------------------------
# MISC - Cài đặt khác
# -----------------------------------------------------
# Window manager settings
FOLLOW_MOUSE_FOCUS: Final[bool] = True
BRING_FRONT_CLICK: Final[bool] = True
CURSOR_WARP: Final[bool] = False  # Đưa chuột vào giữa màn hình khi chuyển workspace
AUTO_FULLSCREEN: Final[bool] = True
FOCUS_ON_WINDOW_ACTIVATION: Final[str] = "smart"  # Cách thức focus vào cửa sổ
RECONFIGURE_SCREENS: Final[bool] = True
AUTO_MINIMIZE: Final[bool] = True
WM_NAME: Final[str] = "LG3D"

# Redshift settings
REDSHIFT_TEMP_NIGHT: Final[int] = 4500  # Nhiệt độ màu ban đêm (Kelvin)
REDSHIFT_TEMP_DAY: Final[int] = 6500  # Nhiệt độ màu ban ngày (Kelvin)

# Sticky window settings
STICKY_WINDOWS: List[Any] = []  # Danh sách cửa sổ sticky
