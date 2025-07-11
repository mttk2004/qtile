from libqtile import widget, qtile
import subprocess

from modules.settings import font_family, font_size, default_font, default_fontsize, assets_dir, icons_dir, app_launcher
from themes.colors import colors

# Utility functions
def open_launcher():
    qtile.cmd_spawn(app_launcher)

def open_btop():
    qtile.cmd_spawn("wezterm --hold -e btop")

def get_battery_status():
    try:
        output = subprocess.check_output(["acpi", "-b"]).decode().strip()
        percentage = output.split(", ")[1].rstrip("%")
        if "Charging" in output:
            return f"🔌 {percentage}%"
        else:
            return f"🔋 {percentage}%"
    except:
        return "🔋 N/A"

def get_brightness():
    try:
        output = subprocess.check_output(["brightnessctl", "info"]).decode().strip()
        percentage = output.split("(")[1].split("%")[0]
        return f"💡 {percentage}%"
    except:
        return "💡 N/A"

def init_widgets_defaults():
    return dict(
        font=default_font,
        fontsize=default_fontsize,
        padding=4,
    )

def init_widgets_list():
    widgets_list = [
        widget.Spacer(
            length=18,
            background=colors["bar_bg"],
        ),

        widget.Image(
            filename=f'{assets_dir}launch_Icon.png',
            background=colors["bar_bg"],
            mouse_callbacks={'Button1': open_launcher},
        ),

        widget.Image(
            filename=f'{assets_dir}6.png',
        ),

        widget.GroupBox(
            fontsize=16,
            borderwidth=0,
            highlight_method='block',
            active=colors["active"],  # Active workspaces circle color
            block_highlight_text_color=colors["highlight"],  # Current workspace circle color
            highlight_color='#4B427E',
            inactive=colors["inactive"],  # Empty workspace circle
            foreground=colors["bar_fg"],
            background=colors["bar_fg"],
            this_current_screen_border=colors["this_current"],  # Circle background color
            this_screen_border='#52548D',
            other_current_screen_border='#52548D',
            other_screen_border='#52548D',
            urgent_border='#52548D',
            rounded=True,
            disable_drag=True,
        ),

        widget.Image(
            filename=f'{assets_dir}5.png',
        ),

        widget.Image(
            filename=f'{assets_dir}2.png',
        ),

        widget.CurrentLayoutIcon(
            background=colors["bar_fg"],
            padding=4,
            scale=0.5,
        ),

        widget.CurrentLayout(
            background=colors["bar_fg"],
            font=font_family,
            fontsize=font_size,
            padding=0,
        ),

        widget.Image(
            filename=f'{assets_dir}5.png',
        ),

        widget.Image(
            filename=f'{assets_dir}2.png',
        ),

        widget.WindowName(
            background=colors["bar_fg"],
            format="{name}",
            font=font_family,
            fontsize=14,
            empty_group_string='Desktop',
            padding=0,
        ),

        widget.Image(
            filename=f'{assets_dir}5.png',
        ),

        widget.Image(
            filename=f'{assets_dir}2.png',
            background='#52548D',
        ),

        widget.Systray(
            background=colors["bar_fg"],
            icon_size=24,
            padding=3,
        ),

        widget.Image(
            filename=f'{assets_dir}5.png',
        ),

        widget.Image(
            filename=f'{assets_dir}2.png',
            background='#52548D',
        ),

        widget.Spacer(
            length=0,
            background=colors["bar_fg"],
        ),

        # Nhóm thông tin hệ thống: CPU, RAM, Pin, Độ sáng, Âm lượng
        widget.Memory(
            format='RAM:({MemUsed:.0f}MB/{MemTotal:.0f}MB)',
            font=font_family,
            fontsize=font_size,
            padding=0,
            background=colors["bar_fg"],
            mouse_callbacks={'Button1': open_btop},
        ),

        widget.Spacer(
            length=6,
            background=colors["bar_fg"],
        ),

        widget.CPU(
            font=font_family,
            format='CPU:({load_percent:.1f}%/{freq_current}GHz)',
            fontsize=font_size,
            margin=0,
            padding=0,
            background=colors["bar_fg"],
            mouse_callbacks={'Button1': open_btop},
        ),

        widget.Spacer(
            length=6,
            background=colors["bar_fg"],
        ),

        # Alternative battery widget if Battery widget doesn't work
        # widget.GenPollText(
        #     background=theme["foreground"],
        #     font=font_family,
        #     fontsize=font_size,
        #     func=get_battery_status,
        #     padding=0,
        #     update_interval=30,
        # ),

        widget.Battery(
            background=colors["bar_fg"],
            font=font_family,
            fontsize=font_size,
            format='🔋{percent:2.0%}',
            padding=0,
            charge_char='🔌',
            discharge_char='🔋',
            update_interval=30,
            show_short_text=False,
            battery_name='BAT0',
            execute_polling=True,
        ),

        widget.Spacer(
            length=6,
            background=colors["bar_fg"],
        ),

        # Alternative brightness widget if Backlight widget doesn't work
        # widget.GenPollText(
        #     background=theme["foreground"],
        #     font=font_family,
        #     fontsize=font_size,
        #     func=get_brightness,
        #     padding=0,
        #     update_interval=5,
        # ),

        widget.Backlight(
            background=colors["bar_fg"],
            font=font_family,
            fontsize=font_size,
            backlight_name='amdgpu_bl0',
            format='💡{percent:2.0%}',
            padding=0,
            change_command='brightnessctl s {0}%',
            step=5,
        ),

        widget.Spacer(
            length=6,
            background=colors["bar_fg"],
        ),

        widget.Image(
            filename=f'{icons_dir}volume.svg',
            background=colors["bar_fg"],
            margin_y=3,
            scale=True,
            mouse_callbacks={'Button1': open_btop},
        ),

        widget.Spacer(
            length=4,
            background=colors["bar_fg"],
        ),

        widget.PulseVolume(
            font=font_family,
            fontsize=font_size,
            padding=0,
            background=colors["bar_fg"],
        ),

        widget.Image(
            filename=f'{assets_dir}5.png',
        ),

        widget.Image(
            filename=f'{assets_dir}1.png',
            background='#4B427E',
        ),

        widget.Image(
            filename=f'{icons_dir}calendar.svg',
            background=colors["bar_fg"],
            margin_y=3,
            scale=True,
        ),

        widget.Spacer(
            length=6,
            background=colors["bar_fg"],
        ),

        widget.Clock(
            format='%d/%m/%y ',  # Here you can change between USA or another timezone
            background=colors["bar_fg"],
            font=font_family,
            fontsize=font_size,
            padding=0,
        ),

        widget.Image(
            filename=f'{icons_dir}clock.svg',
            background=colors["bar_fg"],
            margin_y=3,
            margin_x=5,
            scale=True,
        ),

        widget.Clock(
            format='%H:%M',
            background=colors["bar_fg"],
            font=font_family,
            fontsize=font_size,
            padding=0,
        ),

        widget.Spacer(
            length=18,
            background=colors["bar_fg"],
        ),
    ]
    return widgets_list
