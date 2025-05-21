# Settings for Qtile configuration

# System settings
mod = "mod4" # Windows key
mod1 = "mod1" # Alt key
terminal = "alacritty"
filemanager = "thunar"
app_launcher = "rofi -theme rounded-green-dark -show drun"  # Lệnh mở menu drun

# GPU Screen Recorder
gpu_screen_recorder = "flatpak run com.dec05eba.gpu_screen_recorder"

# Appearance
font_family = "CaskaydiaCove Nerd Font SemiBold"
font_size = 18
default_font = "sans"
default_fontsize = 16

# Bar appearance
bar_height = 40
bar_margin = [0, 8, 6, 8]  # [Top, Right, Bottom, Left]

# Colors
theme = {
    "background": "#033C4B",
    "foreground": "#046F5F",
    "focus": "#00DC6C",
    "normal": "#1F1D2E",
    "highlight": "#00F076",
    "active": "#56D9C7",
    "inactive": "#052A25",
    "current_screen_border": "#00361A",
    "other_screen_border": "#52548D",
}

# Assets paths
assets_dir = "~/.config/qtile/Assets/"
icons_dir = f"{assets_dir}Bar-Icons/"

# Scripts paths
scripts_dir = "~/.config/qtile/scripts/"
powermenu_script = f"{scripts_dir}powermenu.sh"
ksnipmenu_script = f"{scripts_dir}ksnipmenu.sh"
autostart_script = f"{scripts_dir}autostart.sh"

# Redshift settings
redshift_temp_night = 4500  # Nhiệt độ màu ban đêm (Kelvin)
