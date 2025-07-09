from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy

from modules.settings import (
    MOD, MOD_ALT, TERMINAL, FILEMANAGER, POWERMENU_SCRIPT,
    APP_LAUNCHER, GPU_SCREEN_RECORDER, KSNIPMENU_SCRIPT,
    STICKY_WINDOWS
)



@lazy.function
def toggle_sticky_windows(qtile, window=None):
    if window is None:
        window = qtile.current_screen.group.current_window
    if window in STICKY_WINDOWS:
        STICKY_WINDOWS.remove(window)
    else:
        STICKY_WINDOWS.append(window)
    return window



def init_keys():
    keys = [
        # A list of available commands that can be bound to keys can be found
        # at https://docs.qtile.org/en/latest/manual/config/lazy.html
        # Switch between windows
        Key([MOD], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([MOD], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([MOD], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([MOD], "Up", lazy.layout.up(), desc="Move focus up"),
        Key([MOD], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([MOD], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([MOD], "j", lazy.layout.down(), desc="Move focus down"),
        Key([MOD], "k", lazy.layout.up(), desc="Move focus up"),
        Key([MOD], "space", lazy.layout.next(), desc="Move window focus to other window"),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key([MOD, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([MOD, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([MOD, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([MOD, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key([MOD, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([MOD, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([MOD, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([MOD, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([MOD], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        Key([MOD], "f", lazy.window.toggle_fullscreen(), desc="Toggle focused window to fullscreen"),
        Key([MOD, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
        Key([MOD, "shift"], "c", lazy.window.center(), desc="Center floating window"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [MOD, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([MOD], "Return", lazy.spawn(TERMINAL), desc="Launch terminal"),
        Key([MOD, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

        # Window switcher
        Key([MOD], "Tab", lazy.spawn("rofi -theme ~/.config/qtile/themes/rofi/modern-green-window.rasi -show window -show-icons"), desc="Switch windows with Rofi"),

        Key([MOD], "q", lazy.window.kill(), desc="Kill focused window"),
        # System Controls KeyChord
        KeyChord([MOD], "c", [
            Key([], "r", lazy.reload_config(), desc="Reload the config"),
            Key([], "q", lazy.shutdown(), desc="Shutdown Qtile"),
            Key([], "p", lazy.spawn(f"fish -c '{POWERMENU_SCRIPT}'"), desc="Show power menu"),
        ], name="System"),
        Key([MOD], "d", lazy.spawn(APP_LAUNCHER), desc="Open application launcher"),

        # Chuyển đổi giữa các workspace liền kề
        Key([MOD, "mod1"], "Left", lazy.screen.prev_group(), desc="Chuyển đến workspace bên trái"),
        Key([MOD, "mod1"], "Right", lazy.screen.next_group(), desc="Chuyển đến workspace bên phải"),

    ##CUSTOM
        Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +1%"), desc='Volume Up'),
        Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -1%"), desc='volume down'),
        Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc='Volume Mute'),
        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc='playerctl'),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc='playerctl'),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc='playerctl'),
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl s 5%+"), desc='brightness UP'),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl s 5%-"), desc='brightness Down'),
        Key([], "XF86TouchpadToggle", lazy.spawn("sh -c 'xinput --list-props \"$(xinput --list --name-only | grep -i Touchpad)\" | grep \"Device Enabled\" | awk \'{print $NF}\' | xargs -I {} xinput --set-prop \"$(xinput --list --name-only | grep -i Touchpad)\" \"Device Enabled\" $((1-{}))'"), desc="Toggle touchpad"),

    ##Misc keybinds
        Key([], "Print", lazy.spawn(f"fish -c 'flameshot'"), desc='Screenshot with Flameshot'),
        Key([MOD, "control"], "p", lazy.spawn(f"fish -c '{KSNIPMENU_SCRIPT}'"), desc='Screenshot Menu'),
        Key([MOD], "e", lazy.spawn(FILEMANAGER), desc="Open file manager"),
        Key([MOD], "s", toggle_sticky_windows, desc="Toggle state of sticky for current window"),
        Key([MOD], "g", lazy.spawn(GPU_SCREEN_RECORDER), desc="Open GPU Screen Recorder"),
    ]

    # Phím tắt cho Scratchpads
    keys.extend([
        Key([MOD], "F12", lazy.group['scratchpad'].dropdown_toggle('files'), desc="Toggle scratchpad file manager"),
        Key([MOD], "F11", lazy.group['scratchpad'].dropdown_toggle('term'), desc="Toggle scratchpad terminal"),
        Key([MOD], "F10", lazy.group['scratchpad'].dropdown_toggle('monitor'), desc="Toggle scratchpad system monitor"),
    ])

    return keys
