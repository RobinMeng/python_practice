import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import qtUI


class MyMainWindow(QMainWindow):
    """自定义槽函数"""

    def __init__(self):
        super().__init__()
        self.ui = qtUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn1.clicked.connect(self.showMessage)

    def showMessage(self):
        QMessageBox.question(self.ui.centralwidget, 'TEST', '请做出你的选择',
                             QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = MyMainWindow()
    windows.show()
    sys.exit(app.exec_())
