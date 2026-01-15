import sys

from PyQt5.QtGui import QValidator, QRegExpValidator, QIntValidator
from PyQt5.QtWidgets import QMainWindow, QApplication
import qtUI


class MyMainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = qtUI.Ui_MainWindow()
        nameValidator = QIntValidator()
        nameValidator.setRange(1, 100)
        self.ui.lineEditName.setValidator(nameValidator)
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindows = MyMainWindows()
    mywindows.show()
    sys.exit(app.exec_())
