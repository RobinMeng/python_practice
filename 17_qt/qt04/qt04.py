import sys
import qtUI

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    ## 自动配置信号和槽
    app = QApplication(sys.argv)
    windows = QMainWindow()
    ui = qtUI.Ui_MainWindow()
    ui.setupUi(windows)
    windows.show()
    sys.exit(app.exec_())
