#!/bin/bash

# Get the directory of the script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Directory containing the script to be copied
SOURCE_DIR="$SCRIPT_DIR"

# Name of the script to be copied
SCRIPT_NAME="chillfetch.py"

# Directory in PATH where the symlink will be created
TARGET_DIR="/usr/local/bin"

# Check if the script exists and is executable
if [ ! -x "$SOURCE_DIR/$SCRIPT_NAME" ]; then
    echo "Error: Script is not executable or does not exist: $SOURCE_DIR/$SCRIPT_NAME"
    exit 1
fi

# Create a symbolic link to the script in the target directory with sudo
sudo ln -sf "$SOURCE_DIR/$SCRIPT_NAME" "$TARGET_DIR/chillfetch"

# Ensure symlink was created successfully
if [ $? -eq 0 ]; then
    echo "Script symlinked to PATH: $TARGET_DIR"
else
    echo "Error creating symlink in PATH: $TARGET_DIR"
    exit 1
fi
