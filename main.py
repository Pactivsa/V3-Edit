import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import openpyxl as op
from pathlib import Path
import shutil
import pyperclip

# 这是一个示例 Python 脚本。
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

SRC_PATH = Path.absolute(Path(__file__)).parent


# file_path = str(SRC_PATH / "a/b.ui")
# todo: 不要引相对路径。打包时会有问题，把所有相对路径都改成上面的格式。

class OpeningUI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(str(SRC_PATH / "./main.ui"))


class MainUI(QMainWindow):
    # 幽默主界面
    # todo 美化

    # 实体化 #
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    # 定义界面 #
    def init_ui(self):
        self.ui = uic.loadUi("./UI/main.ui")
        print(self.ui.action_About)

        # 调取UI控件
        action_about = self.ui.action_About
        action_tool_export_goods = self.ui.action_Tool_export_Goods
        action_tool_import = self.ui.action_Tool_import

        # 定义信号，连接槽函数
        action_about.triggered.connect(self.act_about)
        action_tool_export_goods.triggered.connect(self.act_export_goods)
        action_tool_import.triggered.connect(self.act_import_goods)

    # 定义槽函数 #
    def act_export_goods(self):
        # 幽默展示和隐藏
        main_table1.ui.show()
        main_table2.ui.hide()
        # ...

    def act_import_goods(self):
        main_table1.ui.hide()
        main_table2.ui.show()

    def act_about(self):
        msgbox = QMessageBox(QMessageBox.Information, "关于", "V3编辑器\n由小草青青、VK8040、恋恋的钢盔共同制作",
                             QMessageBox.Ok, self)
        msgbox.show()


class MainTable_export_goods(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./UI/export_goods.ui")
        # todo 补


class MainTable_import_goods(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./UI/import_goods.ui")
        # todo 补


class MainTable_PM(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(str(SRC_PATH / "./main.ui"))


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = QApplication(sys.argv)

    opening = OpeningUI()
    main_ui = MainUI()
    main_table1 = MainTable_export_goods()
    main_table2 = MainTable_import_goods()
    main_table3 = MainTable_PM()
    opening.ui.show()

    app.exec()
