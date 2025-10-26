import sys

from PySide6.QtWidgets import QApplication

from src import gui, brightness_service


def main():
    check = brightness_service.check_brightnessctl()
    if not check:
        return check
    else:
        app = QApplication(sys.argv)
        app.setStyleSheet(dark_mode) #Default : dark_mode but you can choose from light_mode,dark_mode and everforest
        # Create and show main window
        window = gui.MyWindow()
        window.show()

        # Run application
        sys.exit(app.exec())



everforest = """
        QMainWindow {
            background-color: #2b3339;
            color: #d3c6aa;
        }

        QLabel {
            color: #d3c6aa;
            font-size: 14px;
        }

        QSlider::groove:horizontal {
            height: 6px;
            background: #414b50;
            border-radius: 3px;
        }

        QSlider::handle:horizontal {
            background: #a7c080;
            width: 14px;
            margin: -5px 0;
            border-radius: 7px;
        }

        QSlider::sub-page:horizontal {
            background: #a7c080;
            border-radius: 3px;
        }

        QPushButton {
            background-color: #3a464c;
            color: #d3c6aa;
            border: 1px solid #4f585e;
            border-radius: 5px;
            padding: 6px;
        }

        QPushButton:hover {
            background-color: #505a60;
        }

        QPushButton:pressed {
            background-color: #a7c080;
            color: #2b3339;
        }

        QToolTip {
            background-color: #414b50;
            color: #d3c6aa;
            border: 1px solid #a7c080;
        }
    """
dark_mode = """
        QMainWindow {
            background-color: #1e1e1e;
            color: #d4d4d4;
        }
        QLabel {
            color: #ffffff;
            font-size: 14px;
        }
        QSlider::groove:horizontal {
            height: 6px;
            background: #333333;
            border-radius: 3px;
        }
        QSlider::handle:horizontal {
            background: #00bcd4;
            width: 14px;
            margin: -5px 0;
            border-radius: 7px;
        }
        QSlider::sub-page:horizontal {
            background: #00bcd4;
            border-radius: 3px;
        }
        QPushButton {
            background-color: #333333;
            color: white;
            border: 1px solid #555555;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #444444;
        }
        QPushButton:pressed {
            background-color: #00bcd4;
        }
    """
light_mode = """

        QMainWindow {
            background-color: #f3f3f3;
            color: #333333;
        }

        QLabel {
            color: #333333;
            font-size: 14px;
        }

        QSlider::groove:horizontal {
            height: 6px;
            background: #dcdcdc;
            border-radius: 3px;
        }

        QSlider::handle:horizontal {
            background: #007acc;
            width: 14px;
            margin: -5px 0;
            border-radius: 7px;
        }

        QSlider::sub-page:horizontal {
            background: #007acc;
            border-radius: 3px;
        }

        QPushButton {
            background-color: #e6e6e6;
            color: #333333;
            border: 1px solid #cccccc;
            border-radius: 5px;
            padding: 6px;
        }

        QPushButton:hover {
            background-color: #dcdcdc;
        }

        QPushButton:pressed {
            background-color: #007acc;
            color: white;
        }

        QToolTip {
            background-color: #f9f9f9;
            color: #333333;
            border: 1px solid #cccccc;
        }
    """
if __name__ == '__main__':
    main()
