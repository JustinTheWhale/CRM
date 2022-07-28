from PyQt5 import QtWidgets

from db import *


class Combo_Dialog(QtWidgets.QWidget):
    def __init__(self, c_id):
        super().__init__()
        self.title = "Combo Dialog"
        self.left = 540
        self.top = 270
        self.width = 100
        self.height = 100
        self.selection = None
        self.c_id = c_id
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getChoice(self.c_id)
        self.show()

    def getChoice(self, c_id):
        if c_id == None:
            categories = get_all_categories()
            item, Okpressed = QtWidgets.QInputDialog.getItem(
                self,
                "Add to Existing Category",
                "Select one from the list:",
                categories,
                0,
                False,
            )
            if Okpressed and item:
                self.selection = item
        else:
            categories = get_all_categories(self.c_id).split(";")
            item, Okpressed = QtWidgets.QInputDialog.getItem(
                self,
                "Remove Category from Client:",
                "Select one from the list:",
                categories,
                0,
                False,
            )
            if Okpressed and item:
                self.selection = item


class Input_Dialog(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Combo Dialog"
        self.left = 540
        self.top = 270
        self.width = 100
        self.height = 100
        self.text = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getInput()
        self.show()

    def getInput(self):
        text, Okpressed = QtWidgets.QInputDialog.getText(
            self,
            "Add New Category",
            "Input the name of the new category here:",
            QtWidgets.QLineEdit.Normal,
            "",
        )
        if Okpressed and text != "":
            self.selection = text


class Category_Dialog(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Combobox Dialog"
        self.left = 540
        self.top = 270
        self.width = 100
        self.height = 100
        self.selection = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.getChoice()
        self.show()

    def getChoice(self):
        categories = get_all_categories()
        item, Okpressed = QtWidgets.QInputDialog.getItem(
            self, "Remove Category", "Select one from the list:", categories, 0, False
        )
        if Okpressed and item:
            self.selection = item
