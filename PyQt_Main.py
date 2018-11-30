import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt_AirQualityToolkit import Ui_MainWindow

class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
app.exec_()
