# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Import modules
from modules.keys import init_keys
from modules.groups import init_groups, init_group_keys
from modules.layouts import init_layouts, init_floating_layout
from modules.mouse import init_mouse
from modules.screens import init_screens
import modules.hooks

# Initialize Qtile components
keys = init_keys()
groups = init_groups()
keys = init_group_keys(groups, keys)
layouts = init_layouts()
floating_layout = init_floating_layout()
mouse = init_mouse()
screens = init_screens()

# Additional configuration
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False  # This puts your mouse in the center on the screen after you switch to another workspace
auto_fullscreen = True
focus_on_window_activation = "smart"  # or focus
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None

# LG3D is a 3D non-reparenting WM written in java that happens to be on java's whitelist.
wmname = "LG3D"
