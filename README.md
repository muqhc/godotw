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

### project.godotw.toml

```toml
[godot]
version = "4.6"             # required
mono-required = false       # optional, default is false
release-status = "stable"   # optional, default is "stable"
```

### commands

you can use godot.bat or godot.sh 

general options:

- [--local]: use local godot management directory (./.godotw)
  - without this option, the management dir is ((USERPROFILE)/.godotw)
- [--install]: install godot from github before executing

commands:

- ./godotw.sh open

- ./godotw.sh run

- ./godotw.sh setup vscode [--symlink] [--godot-tools]

- ./godotw.sh setup symlink

- ./godotw.sh --install
