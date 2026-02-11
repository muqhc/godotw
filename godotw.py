"""
This is python script to link godot project with right version of godot godot executable,
by reading project.godotw.toml.
This script is almost delegation of the godot godot executable.
This script will be included in godot project folder.
The godot godot executable is usually in the user's home directory. (.godotw/godots/{godot-name}/{godot-name}.exe) (.exe is for windows, it will be different for other platforms)
(platforms: win32, win64, window_arm64, linux.x86_32, linux.x86_64, linux.arm32, linux.arm64, macos.universal)
(platforms(.net-mono-support): mono_win32, mono_win64, mono_window_arm64, mono_linux_x86_32, mono_linux_x86_64, mono_linux_arm32, mono_linux_arm64, mono_macos.universal)
"""

import os
import tomllib
import platform
from typing import Any
from pathlib import Path
import sys
import subprocess
import json

args = sys.argv[1:]

project_toml_path = "project.godotw.toml"

with open(project_toml_path, "rb") as f:
    project_toml = tomllib.load(f)

table_godot: dict[str, Any] = project_toml["godot"]

godot_version: str = table_godot["version"]
is_required_mono: bool = table_godot.get("mono-required", False)
godot_release_status: str = table_godot.get("release-status", "stable")

def get_platform_names() -> list[str]:
    match platform.system():
        case "Windows":
            if "arm" in platform.machine().lower():
                return ["windows_arm64.exe", "windows_arm64"]
            if "64" in platform.machine():
                return ["win64.exe", "win64"]
            else:
                return ["win32.exe", "win32"]
        case "Linux":
            if "arm" in platform.machine().lower():
                return ["linux.arm64","linux_arm64"]
            elif "64" in platform.machine():
                return ["linux.x86_64","linux_x86_64"]
            else:
                return ["linux.x86_32","linux_x86_32"]
        case "Darwin":
            return ["macos.universal"]
        case _:
            raise ValueError(f"Unsupported platform: {platform.system()}")


platform_names = get_platform_names()

godot_names = os.listdir(Path.home().joinpath(".godotw/godots/"))

available_godots = [name for name in godot_names if name.startswith(f"Godot_v{godot_version}-{godot_release_status}") and any(platform_name in name for platform_name in platform_names) and (not is_required_mono or "mono" in name)]

if not available_godots:
    print(f"No available godot found for version {godot_version} and platform {platform_names}")
    if "--install" in args:
        print(f"Installing godot {godot_version} from github...")
        
        import urllib.request

        name = f"Godot_v{godot_version}-{godot_release_status}{'_mono' if is_required_mono else ''}_{platform_names[0 if not is_required_mono else -1]}"
        url = f"https://github.com/godotengine/godot/releases/download/{godot_version}-{godot_release_status}/{name}.zip"
        dirpath = Path.home().joinpath(".godotw/godots")
        zippath = Path(dirpath).joinpath(f"{name}.zip")
        godotpath = Path(dirpath).joinpath(f"{name}")

        print(f"Downloading {url}...")
        dirpath.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, zippath)

        # unzip
        print(f"Unzipping {name}...")
        import zipfile

        with zipfile.ZipFile(zippath, "r") as zip_ref:
            zip_ref.extractall(godotpath)
        print(f"Installed {name}.")
    else:
        print(f"If you want install godot, please run 'godotw --install'")
    sys.exit(1)

chosen_godot = available_godots[-1]

godot_path = Path.home().joinpath(f".godotw/godots/{chosen_godot}/{chosen_godot}.exe")
godot_dir = Path.home().joinpath(f".godotw/godots/{chosen_godot}")

def setup_symlink():
    Path("./.godotw").mkdir(parents=True, exist_ok=True)
    if os.path.exists("./.godotw/godot"):
        os.remove("./.godotw/godot")
    os.symlink(godot_dir, "./.godotw/godot", target_is_directory=True)

def setup_vscode_godot_tools(target_path: str):
    Path("./.vscode").mkdir(parents=True, exist_ok=True)
    if os.path.exists("./.vscode/settings.json"):
        with open("./.vscode/settings.json", "r") as f:
            settings = json.load(f)
    else:
        settings = {}
    settings["godotTools.editorPath.godot4"] = target_path 
    with open("./.vscode/settings.json", "w") as f:
        json.dump(settings, f, indent=4)

if len(args) > 0 and args[0] == "setup":
    if len(args) > 1 and args[1] == "symlink":
        #make symbolic link to godot directory
        setup_symlink()
    if len(args) > 1 and args[1] == "vscode":
        target_path: str
        if "--symlink" in args:
            setup_symlink()
            target_path = f"./.godotw/godot/{chosen_godot}.exe"
        else:
            target_path = godot_path.absolute().as_posix()
        if "--godot-tools" in args:
            setup_vscode_godot_tools(target_path)
        else:
            setup_vscode_godot_tools(target_path)
else:
    subprocess.run([godot_path]+args)

