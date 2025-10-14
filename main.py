import sys

from PySide6.QtWidgets import QApplication

import brightness_service
import gui

def main():
    check = brightness_service.check_brightnessctl()
    if not check:
        return check
    else:
        app = QApplication(sys.argv)

        # Create and show main window
        window = gui.MyWindow()
        window.show()

        # Run application
        sys.exit(app.exec())

if __name__ == '__main__':
    main()