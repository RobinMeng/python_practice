import sys  # 提供解释器相关操作，如命令行参数和退出码
import qtui01  # 导入由 pyuic5 生成的界面类（qtui01.py 中的 Ui_MainWindow）

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    # 1. 创建 Qt 应用程序对象，必须最先执行
    app = QApplication(sys.argv)

    # 2. 实例化一个空的主窗口（QMainWindow），后面再把界面“贴”上去
    mainwindow = QMainWindow()

    # 3. 实例化 pyuic5 生成的界面类，并调用 setupUi 把界面绑定到主窗口
    ui = qtui01.Ui_MainWindow()
    ui.setupUi(mainwindow)

    # 4. 显示主窗口
    mainwindow.show()

    # 5. 进入 Qt 事件循环；程序会一直运行直到窗口关闭
    sys.exit(app.exec_())
