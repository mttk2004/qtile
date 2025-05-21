"""
Cấu hình bố cục cửa sổ hiện đại cho Qtile.

Sử dụng bảng màu từ themes/colors.py.
"""

from libqtile import layout
from libqtile.config import Match

from themes.colors import colors

def init_layouts():
    """Khởi tạo danh sách layouts.

    Sử dụng các layout hiện đại với thiết kế tối giản và hiệu quả.
    """
    layouts = [
        # Layout Columns - Bố cục cột, phù hợp cho nhiều cửa sổ
        layout.Columns(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=2,
            border_on_single=False,
            margin=6,
            margin_on_single=6,
            grow_amount=2,
            insert_position=1,  # Thêm cửa sổ mới vào vị trí sau cửa sổ hiện tại
        ),

        # Layout Max - Phóng to cửa sổ hiện tại
        layout.Max(),

        # Layout MonadTall - Bố cục cửa sổ chính ở bên trái, các cửa sổ khác ở bên phải
        layout.MonadTall(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=2,
            margin=6,
            ratio=0.6,
            min_ratio=0.30,
            max_ratio=0.70,
            change_ratio=0.05,
        ),

        # Layout MonadWide - Bố cục cửa sổ chính ở trên, các cửa sổ khác ở dưới
        layout.MonadWide(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=2,
            margin=6,
            ratio=0.6,
        ),

        # Layout Matrix - Bố cục dạng lưới
        layout.Matrix(
            border_focus=colors["border_focus"],
            border_normal=colors["border_normal"],
            border_width=2,
            margin=6,
        ),

        # Layout TreeTab - Bố cục dạng cây
        layout.TreeTab(
            active_bg=colors["green_primary"],
            active_fg=colors["bg"],
            bg_color=colors["bg"],
            font="JetBrains Mono",
            fontsize=12,
            inactive_bg=colors["inactive"],
            inactive_fg=colors["fg"],
            padding_left=6,
            padding_x=6,
            padding_y=6,
            sections=["Tabs"],
            section_fontsize=12,
            section_fg=colors["green_accent"],
            section_top=15,
            panel_width=200,
        ),
    ]
    return layouts

def init_floating_layout():
    """Khởi tạo layout nổi.

    Cấu hình cho các cửa sổ nổi.
    """
    floating_layout = layout.Floating(
        border_focus=colors["border_focus"],
        border_normal=colors["border_normal"],
        border_width=2,
        float_rules=[
            # Thêm các quy tắc cho các cửa sổ nổi
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
            Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
            Match(wm_class="Galculator"),  # Calculator
            Match(wm_class="Gpick"),  # Color picker
            Match(wm_class="Nitrogen"),  # Wallpaper setter
            Match(wm_class="Lxappearance"),  # Theme setter
            Match(wm_class="Pavucontrol"),  # Audio control
            Match(wm_class="Xfce4-terminal"),  # Terminal with specific class
            Match(wm_class="Thunar", title="File Operation Progress"),  # Thunar file operations
        ],
    )
    return floating_layout
