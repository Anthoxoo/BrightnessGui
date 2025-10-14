import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QSlider, QPushButton, QLabel, QApplication
import brightness_service as b

class MyWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Brightnessctl GUI')
        self.resize(320, 150)

        #Slider related
        self.__slider = QSlider(Qt.Horizontal, self)
        self.__slider.setGeometry(10, 50, 250, 40)
        self.__slider.setMinimum(1)  # avoid 0% brightness
        self.__slider.setMaximum(100)
        self.__slider.valueChanged.connect(self.valueChanged)

        self.__label = QLabel(self)
        self.__label.setGeometry(270, 50, 40, 40)
        self.__label.setAlignment(Qt.AlignCenter)

        #Show the current brightness at start
        current = b.show_brightness_percentage()
        if current is not None:
            self.__slider.setValue(current)
            self.__label.setText(f"{current}%")
        else:
            self.__label.setText("Error")
    def valueChanged(self, value):
        self.__label.setText(str(value) + "%")
        b.set_brightness(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())