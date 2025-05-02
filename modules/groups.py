from libqtile.config import Group, Key
from libqtile.lazy import lazy

from modules.settings import mod

def init_groups():
    groups = [Group(f"{i+1}", label="⬤") for i in range(9)]
    return groups

def init_group_keys(groups, keys):
    for i in groups:
        keys.extend(
            [
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc=f"Switch to group {i.name}",
                ),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc=f"Switch to & move focused window to group {i.name}",
                ),
            ]
        )
    return keys
