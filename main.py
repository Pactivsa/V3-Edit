import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import openpyxl as op
from pathlib import Path
import shutil
import pyperclip
from utils.backend import BackendManager
from API.building import *
from template.buildings import *
import os
import ast

# 这是一个示例 Python 脚本。
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

SRC_PATH = Path.absolute(Path(__file__)).parent


# file_path = str(SRC_PATH / "a/b.ui")
# todo: 不要引相对路径。打包时会有问题，把所有相对路径都改成上面的格式。

def copy_folder(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    for item in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, item)):
            shutil.copy(os.path.join(source_folder, item), destination_folder)
        else:
            copy_folder(os.path.join(source_folder, item), os.path.join(destination_folder, item))


class OpeningUI(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()
        self.folder = None

    def init_ui(self):
        print(str(SRC_PATH / "./UI/opening.ui"))
        self.ui = uic.loadUi(str(SRC_PATH / "./UI/opening.ui"))

        pushButton = self.ui.pushButton
        pushButton_2 = self.ui.pushButton_2
        pushButton_3 = self.ui.pushButton_3

        pushButton.clicked.connect(lambda: self.importfolder(self.ui.lineEdit_2))
        pushButton_3.clicked.connect(lambda: self.importfolder(self.ui.lineEdit))
        pushButton_2.clicked.connect(lambda: self.loadv3file(self.ui.lineEdit_2, self.ui.lineEdit))

    def importfolder(self, QlineEdit):
        self.folder = QFileDialog.getExistingDirectory(self, "选择文件夹")
        print(self.folder)
        QlineEdit.setText(self.folder)

    def loadv3file(self, QlineEdit1, QlineEdit2):
        GamePath = QlineEdit1.text()
        ModPath = QlineEdit2.text()

        tempmodpath = str(SRC_PATH / "./mod/test")

        copy_folder(GamePath + '/common', tempmodpath + '/common')
        copy_folder(ModPath + '/common', tempmodpath + '/common')
        BM = BackendManager(GamePath, tempmodpath)
        goods, rowgoods = BM.get_part("goods")
        pm,rowpm = BM.get_part("pm")
        print(BM.get_part("pm"))
        header_labels = ["Name", "Cost"]
        main_ui.ui.tableWidget_2.setHorizontalHeaderLabels(header_labels)

        k = 0
        for i in goods:
            single_goods, rc = get_goods_detail(BM, i)
            single_goods_str = str(single_goods)
            single_goods_dict = ast.literal_eval(single_goods_str)
            main_ui.ui.tableWidget_2.setItem(k, 0, QTableWidgetItem(i))
            main_ui.ui.tableWidget_2.setItem(k, 1, QTableWidgetItem(str(single_goods_dict[i][1]['cost'][1])))
            row_count = main_ui.ui.tableWidget_2.rowCount()  # 返回当前行数(尾部)
            main_ui.ui.tableWidget_2.insertRow(row_count)
            k = k+1
        for j in pm:
            single_pm, rc = get_goods_detail(BM, j)
            single_pm_str = str(single_pm)
            single_pm_dict = ast.literal_eval(single_pm_str)


        # todo: 点击后，根据QlineEdit1（原版路径）与QlineEdit2（MOD路径）读取相关文件（PM与商品），建立相关结构化数据（并将相关数据导入到各个TABLE中）。然后，隐藏opening
        opening.ui.close()
        main_ui.ui.show()
        main_ui.ui.tableWidget1.show()
        #  隐藏并显示MAIN界面。
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
        # todo: 点击添加商品、保存修改、删除商品，分别在对应熟人/输出中添加、修改、删除商品。然后，执行recount()函数。
        # todo: 输入或输出商品改变当前行，同步改变数量EDITLINE中的文本。
        # todo: 建立recount()函数，计算利润率等相关内容，然后显示在相应位置。
        # todo: 点击生成代码并复制按钮，根据输入及输出商品生成代码，并复制在剪贴板上。


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
