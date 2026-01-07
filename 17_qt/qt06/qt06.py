import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from qtUI import Ui_MainWindow


class MyMainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        print(self.ui.label.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MyMainWindows()
    windows.show()
    sys.exit(app.exec_())
    pass
