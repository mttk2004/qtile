from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from modules.settings import mod, mod1, terminal, filemanager, powermenu_script, app_launcher

# Sticky windows
sticky_windows = []

@lazy.function
def toggle_sticky_windows(qtile, window=None):
    if window is None:
        window = qtile.current_screen.group.current_window
    if window in sticky_windows:
        sticky_windows.remove(window)
    else:
        sticky_windows.append(window)
    return window

@lazy.function
def switch_to_prev_group(qtile):
    """Chuyển đến workspace trước đó"""
    current_group_index = qtile.groups.index(qtile.current_group)
    # Nếu đang ở workspace đầu tiên, chuyển đến workspace cuối cùng
    if current_group_index == 0:
        qtile.current_screen.set_group(qtile.groups[-1])
    else:
        qtile.current_screen.set_group(qtile.groups[current_group_index - 1])

@lazy.function
def switch_to_next_group(qtile):
    """Chuyển đến workspace tiếp theo"""
    current_group_index = qtile.groups.index(qtile.current_group)
    # Nếu đang ở workspace cuối cùng, chuyển đến workspace đầu tiên
    if current_group_index == len(qtile.groups) - 1:
        qtile.current_screen.set_group(qtile.groups[0])
    else:
        qtile.current_screen.set_group(qtile.groups[current_group_index + 1])

def init_keys():
    keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle focused window to fullscreen"),
        Key([mod], "v", lazy.window.toggle_floating(), desc="Toggle focused window to floating"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        Key([mod], "d", lazy.spawn(app_launcher), desc="Open application launcher"),

        # Chuyển đổi giữa các workspace liền kề
        Key([mod, mod1], "Left", switch_to_prev_group(), desc="Chuyển đến workspace bên trái"),
        Key([mod, mod1], "Right", switch_to_next_group(), desc="Chuyển đến workspace bên phải"),

    ##CUSTOM
        Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +1%"), desc='Volume Up'),
        Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -1%"), desc='volume down'),
        Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc='Volume Mute'),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc='brightness UP'),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc='brightness Down'),

    ##Misc keybinds
        Key([], "Print", lazy.spawn("flameshot gui"), desc='Screenshot'),
        Key(["control"], "Print", lazy.spawn("flameshot full -c -p ~/Pictures/"), desc='Screenshot'),
        Key([mod], "e", lazy.spawn(filemanager), desc="Open file manager"),
        Key([mod], "s", toggle_sticky_windows(), desc="Toggle state of sticky for current window"),
        Key([mod], "x", lazy.spawn(f"fish -c '{powermenu_script}'"), desc="Show power menu"),
    ]
    return keys
