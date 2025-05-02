# Settings for Qtile configuration

# System settings
mod = "mod4" # Windows key
mod1 = "mod1" # Alt key
terminal = "alacritty"
filemanager = "thunar"

# Appearance
font_family = "IBM Plex Mono Medium"
font_size = 15
default_font = "sans"
default_fontsize = 12

# Bar appearance
bar_height = 30
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
autostart_script = f"{scripts_dir}autostart.sh"

# Redshift settings
redshift_temp_night = 4500  # Nhiệt độ màu ban đêm (Kelvin)
