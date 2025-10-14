#!/bin/bash

echo "╔════════════════════════════════════════╗"
echo "║ Brightness GUI - Uninstallation Script║"
echo "╚════════════════════════════════════════╝"
echo ""

INSTALL_DIR="$HOME/.local/share/brightness-gui"
BIN_FILE="$HOME/.local/bin/brightness-gui"
DESKTOP_FILE="$HOME/.local/share/applications/brightness-gui.desktop"

# Removes the files
echo "🗑️  Removing files..."
rm -rf "$INSTALL_DIR"
rm -f "$BIN_FILE"
rm -f "$DESKTOP_FILE"

# Updates the app database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$HOME/.local/share/applications" 2>/dev/null || true
fi

echo "✅ Uninstallation complete!"
echo ""
echo "Note: brightnessctl and Python dependencies were not removed."
echo "To remove them manually:"
echo "  • brightnessctl: sudo apt remove brightnessctl"
echo "  • PySide6: pip3 uninstall PySide6"