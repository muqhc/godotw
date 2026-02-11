#!/bin/sh

# Determine the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/godotw.py"

# Detect python command
if command -v python3 >/dev/null 2>&1; then
    PY_CMD=python3
else
    PY_CMD=python
fi

if [ "$1" = "setup" ] && [ "$2" = "symlink" ]; then
    # The Windows batch file explicitly changes directory to the script location
    # and requests admin privileges for this specific command.
    cd "$SCRIPT_DIR"
    sudo "$PY_CMD" "godotw.py" "$@"
elif [ "$1" = "open" ]; then
    "$PY_CMD" "$PYTHON_SCRIPT" -e --path .
elif [ "$1" = "run" ]; then
    "$PY_CMD" "$PYTHON_SCRIPT" --path .
else
    "$PY_CMD" "$PYTHON_SCRIPT" "$@"
fi
