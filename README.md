# godotw

simple godot project manager for multiple godot versions.

## features

- open godot project
- run godot project
- setup godot project for vscode
  - support [godot-tools](https://open-vsx.org/extension/geequlim/godot-tools)
- setup symlink of godot to project
- install godot from github

## usage

general options:

- [--install]: install godot from github before executing

commands:

- ./godotw.sh open

- ./godotw.sh run

- ./godotw.sh setup vscode [--symlink] [--godot-tools]

- ./godotw.sh setup symlink

- ./godotw.sh --install