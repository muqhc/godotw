# godotw

simple godot project manager handling multiple godot versions.

it also works as wrapper of correct version of godot, so you can access right godot by same command.

## features

- open godot project
- run godot project
- setup godot project for vscode
  - support [godot-tools](https://open-vsx.org/extension/geequlim/godot-tools)
- setup symlink of godot to project
- install godot from github

## requirement

Python 3 (version >= 3.11)

## usage

copy-paste files (godotw.py, godotw.bat, godotw.sh) to your project

run godotw `setup`

use options (`--local`, `--install`) if you need

configuration files (almost `.toml`) you need will be generated when you run godotw

commands of `setup` are prevent from running actual godot so you use it you need only 'setup' process with godotw

### project.godotw.toml

generating this file requires `project.godot`

if there's no `project.godot`, you need to write it manually or copy-paste from this github repo

```toml
[godot]
version = "4.6"             # required
mono-required = false       # optional, default is false
release-status = "stable"   # optional, default is "stable"
```

### commands

you can use godot.bat or godot.sh 

general options:

- [--local]: use local godot management directory `./.godotw`
  - without this option, the management dir is `(USERPROFILE)/.godotw`
- [--install]: install godot from github before executing if it can not find valid godot

commands:

- ./godotw.sh open [--install] [--local]
- ./godotw.sh run [--install] [--local]
- ./godotw.sh setup [--install] [--local]
- ./godotw.sh setup vscode [--symlink] [--godot-tools]
- ./godotw.sh setup symlink

---

also, godotw delegate godot executable.

for example, `./godotw.sh -e --path .` also works. (add `--local` to link local .godotw)

### .godotw/godotw.toml

this file is supposed to be in the management directory `(USERPROFILE)/.godotw` (`./.godotw` if you want to do `--local`)

```toml
[godot]
repositories = []   # add custom godot storage you made already
```
