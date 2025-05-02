import os
import subprocess
from libqtile import hook

from modules.keys import sticky_windows
from modules.settings import autostart_script

@hook.subscribe.setgroup
def move_sticky_windows():
    for window in sticky_windows:
        window.togroup()
    return

@hook.subscribe.client_killed
def remove_sticky_windows(window):
    if window in sticky_windows:
        sticky_windows.remove(window)

@hook.subscribe.client_managed
def auto_sticky_windows(window):
    info = window.info()
    if (info['wm_class'] == ['Toolkit', 'firefox']
            and info['name'] == 'Picture-in-Picture'):
        sticky_windows.append(window)

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser(autostart_script)
    subprocess.call([home])
