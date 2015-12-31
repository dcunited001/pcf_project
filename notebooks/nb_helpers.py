import os.path
import sys

def fix_pypath():
    cwd = os.getcwd()
    if cwd.endswith("notebooks"):
        proj_dir = os.path.join(cwd,'..')
        if proj_dir not in sys.path:
            sys.path.append(proj_dir)
