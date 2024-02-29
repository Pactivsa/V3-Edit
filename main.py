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
        self.ui = uic.loadUi(str(SRC_PATH / "./UI/opening.ui"))

        pushButton = self.ui.pushButton
        pushButton_2 = self.ui.pushButton_2
        pushButton_3 = self.ui.pushButton_3

        pushButton.clicked.connect(lambda: self.importfolder(self.ui.lineEdit))
        pushButton_3.clicked.connect(lambda: self.importfolder(self.ui.lineEdit_2))
        pushButton_2.clicked.connect(lambda: self.loadv3file(self.ui.lineEdit, self.ui.lineEdit_2))

    def importfolder(self, QlineEdit):
        # todo: 点击后，弹出文件夹选择界面并且在选择后将其显示在QlineEdit中。
        pass

    def loadv3file(self, QlineEdit1, QlineEdit2):
        # todo: 点击后，根据QlineEdit1（原版路径）与QlineEdit2（MOD路径）读取相关文件（PM与商品），建立相关结构化数据。然后，隐藏opening界面并显示MAIN界面。
        pass


class MainUI(QMainWindow):
    # 幽默主界面

    # 实体化 #
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    # 定义界面 #
    def init_ui(self):
        self.ui = uic.loadUi("./UI/main.ui")

        # 调取UI控件
        pushButton_5 = self.ui.pushButton_5
        pushButton_6 = self.ui.pushButton_6
        pushButton_4 = self.ui.pushButton_4
        pushButton_7 = self.ui.pushButton_7
        pushButton_8 = self.ui.pushButton_8
        pushButton_9 = self.ui.pushButton_9
        pushButton = self.ui.pushButton
        pushButton_2 = self.ui.pushButton_2
        pushButton_3 = self.ui.pushButton_3
        tableWidget = self.ui.tableWidget

        # 定义信号，连接槽函数
        pushButton_5.clicked.connect(lambda: self.changepage(self.ui.stackedWidget, self.ui.buildings))
        pushButton_6.clicked.connect(lambda: self.changepage(self.ui.stackedWidget, self.ui.pmgs))
        pushButton_4.clicked.connect(lambda: self.changepage(self.ui.stackedWidget, self.ui.goods))
        pushButton_7.clicked.connect(self.pmtools)
        pushButton_8.clicked.connect(self.act_export_goods)
        pushButton_9.clicked.connect(self.act_import_goods)
        pushButton.clicked.connect(self.delete)
        pushButton_2.clicked.connect(self.add)
        pushButton_3.clicked.connect(self.change)
        tableWidget.itemSelectionChanged.connect(self.itemchange)

    # 定义槽函数 #
    def changepage(self, QstackedWidget, QWidget):
        # todo: 点击按钮，将QstackedWidget中的页面切换为QWidget。
        pass

    def delete(self):
        # todo: 点击按钮，为当前表格删除选中项。
        pass

    def add(self):
        # todo: 点击按钮，为当前表格添加新项。
        pass

    def change(self):
        # todo: 点击按钮，把当前表格选中项的属性修改为相关Editline的属性。
        pass

    def itemchange(self):
        # todo: 改变表格选中项，把新选中项的属性显示在相应Editline中。
        pass

    def act_export_goods(self):
        # 幽默展示和隐藏
        main_table1.ui.show()
        main_table2.ui.hide()
        main_table3.ui.hide()
        # ...

    def act_import_goods(self):
        main_table1.ui.hide()
        main_table2.ui.show()
        main_table3.ui.hide()

    def pmtools(self):
        main_table1.ui.hide()
        main_table2.ui.hide()
        main_table3.ui.show()

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
        super().__init__(main_ui)
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi(str(SRC_PATH / "./UI/main.ui"))


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
