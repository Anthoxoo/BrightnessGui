#!/bin/bash

set -e  # Stops the script if an error is encountered

echo "╔════════════════════════════════════════╗"
echo "║  Brightness GUI - Installation Script ║"
echo "╚════════════════════════════════════════╝"
echo ""

# Checks if the user has python and pip
if ! command -v python3 &> /dev/null || ! command -v pip3 &> /dev/null; then
    echo "❌ Python3 and / or pip3 are not installed, please install it / them before launching the script again."
    exit 1
fi

# Downloading brightnessctl if the user do not have it
if ! command -v brightnessctl &> /dev/null; then
    echo "📦 brightnessctl not found. Would you like to install it ? (y/n)"
    read answer
    if [ "$answer" = y ];then
      echo "📦 Installation..."
      # Detecting which distribution
      if command -v apt &> /dev/null; then
          sudo apt update
          sudo apt install brightnessctl -y
      elif command -v pacman &> /dev/null; then
          sudo pacman -S brightnessctl --noconfirm
      elif command -v dnf &> /dev/null; then
          sudo dnf install brightnessctl -y
      else
          echo "❌ Could not detect package manager. Please install brightnessctl manually."
          exit 1
      fi
      echo "✅ brightnessctl installed"
  elif [ "$answer" = n ];then
    echo "Cancelling the installation. Goodbye !"
    exit 1
  else
    echo "Cannot recognise the character."
    exit 1
  fi
fi

# Installing python dependencies
echo "📦 Installing Python dependencies..."
pip3 install --user -r requirements.txt || {
    echo "❌ Failed to install Python dependencies"
    exit 1
}
echo "✅ Python dependencies installed"

# Creating directories
INSTALL_DIR="$HOME/.local/share/brightness-gui"
BIN_DIR="$HOME/.local/bin"
DESKTOP_DIR="$HOME/.local/share/applications"

mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"
mkdir -p "$DESKTOP_DIR"

# Copying files
echo "📂 Installing files..."
cp -r src/* "$INSTALL_DIR/src"
cp main.py start.sh "$INSTALL_DIR/"
[ -f assets/icon.png ] && cp assets/icon.png "$INSTALL_DIR/"

# Launch script
cat > "$BIN_DIR/brightness-gui" << EOF
#!/bin/bash
cd "$INSTALL_DIR"
python3 main.py "\$@"
EOF

chmod +x "$BIN_DIR/brightness-gui"

# .desktop file
cat > "$DESKTOP_DIR/brightness-gui.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Brightness Control
Comment=Simple GUI for brightnessctl
Exec=$INSTALL_DIR/start.sh
Icon=$INSTALL_DIR/icon.png
Terminal=false
Categories=Utility;Settings;System;
Keywords=brightness;backlight;screen;
EOF

# Updating app database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$DESKTOP_DIR" 2>/dev/null || true
fi

echo ""
echo "╔════════════════════════════════════════╗"
echo "║     ✅ Installation Complete!          ║"
echo "╚════════════════════════════════════════╝"
echo ""
