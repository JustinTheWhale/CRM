# JustinTheWhale
# CRM
# Open source Qt CRM written in Python, usues a PostgreSQL DB to store data
import ast
import datetime
import difflib
import sys
from os import path

import pyperclip
from PyQt5 import QtCore, QtGui, QtWebEngineWidgets, QtWidgets
from win32com.client import Dispatch

from dialog import *
from db import *
from search import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        scriptDir = path.dirname(path.realpath(__file__))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.label_email_history = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_email_history.sizePolicy().hasHeightForWidth()
        )
        self.label_email_history.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_email_history.setFont(font)
        self.label_email_history.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_email_history.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_email_history.setTextFormat(QtCore.Qt.AutoText)
        self.label_email_history.setScaledContents(True)
        self.label_email_history.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.label_email_history.setObjectName("label_email_history")

        self.gridLayout.addWidget(self.label_email_history, 9, 2, 1, 1)
        self.lineedit_phone_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_phone_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_phone_3.setFont(font)
        self.lineedit_phone_3.setObjectName("lineedit_phone_3")
        self.gridLayout.addWidget(self.lineedit_phone_3, 2, 5, 1, 1)

        self.category_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.category_combobox.setMinimumSize(QtCore.QSize(0, 30))
        self.category_combobox.setObjectName("category_combobox")
        self.category_combobox.setFont(font)
        self.category_combobox.currentIndexChanged.connect(self.combo)
        self.gridLayout.addWidget(self.category_combobox, 4, 3, 1, 1)

        self.lineedit_lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_lname.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_lname.setFont(font)
        self.lineedit_lname.setObjectName("lineedit_lname")
        self.gridLayout.addWidget(self.lineedit_lname, 1, 3, 1, 1)

        self.cb_phone_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_phone_2.setText("")
        self.cb_phone_2.setObjectName("cb_phone_2")
        self.gridLayout.addWidget(self.cb_phone_2, 1, 6, 1, 1)

        self.label_phone_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_phone_1.setFont(font)
        self.label_phone_1.setObjectName("label_phone_1")
        self.gridLayout.addWidget(self.label_phone_1, 0, 4, 1, 1)

        self.label_phone_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_phone_2.setFont(font)
        self.label_phone_2.setObjectName("label_phone_2")
        self.gridLayout.addWidget(self.label_phone_2, 1, 4, 1, 1)

        self.label_phone_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_phone_3.setFont(font)
        self.label_phone_3.setObjectName("label_phone_3")
        self.gridLayout.addWidget(self.label_phone_3, 2, 4, 1, 1)

        self.label_company = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_company.setFont(font)
        self.label_company.setObjectName("label_company")
        self.gridLayout.addWidget(self.label_company, 2, 2, 1, 1)

        self.label_street_line_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_street_line_1.setFont(font)
        self.label_street_line_1.setObjectName("label_street_line_1")
        self.gridLayout.addWidget(self.label_street_line_1, 5, 2, 1, 1)

        self.label_street_line_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_street_line_2.setFont(font)
        self.label_street_line_2.setObjectName("label_street_line_1")
        self.gridLayout.addWidget(self.label_street_line_2, 6, 2, 1, 1)

        self.label_city = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_city.setFont(font)
        self.label_city.setObjectName("label_city")
        self.gridLayout.addWidget(self.label_city, 5, 4, 1, 1)

        self.label_state = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.gridLayout.addWidget(self.label_state, 6, 4, 1, 1)

        self.label_zip = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_zip.setFont(font)
        self.label_zip.setObjectName("label_zip")
        self.gridLayout.addWidget(self.label_zip, 6, 6, 1, 1)

        self.lineedit_street_line_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_street_line_1.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_street_line_1.setFont(font)
        self.lineedit_street_line_1.setObjectName("lineedit_street_line_1")
        self.gridLayout.addWidget(self.lineedit_street_line_1, 5, 3, 1, 1)

        self.lineedit_street_line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_street_line_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_street_line_2.setFont(font)
        self.lineedit_street_line_2.setObjectName("lineedit_street_line_2")
        self.gridLayout.addWidget(self.lineedit_street_line_2, 6, 3, 1, 1)

        self.lineedit_city = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_city.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_city.setFont(font)
        self.lineedit_city.setObjectName("lineedit_city")
        self.gridLayout.addWidget(self.lineedit_city, 5, 5, 1, 1)

        self.lineedit_state = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_state.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_state.setFont(font)
        self.lineedit_state.setObjectName("lineedit_state")
        self.gridLayout.addWidget(self.lineedit_state, 6, 5, 1, 1)

        self.lineedit_zip = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_zip.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_zip.setFont(font)
        self.lineedit_zip.setObjectName("lineedit_zip")
        self.gridLayout.addWidget(self.lineedit_zip, 6, 7, 1, 1)

        self.lineedit_company = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_company.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_company.setFont(font)
        self.lineedit_company.setObjectName("lineedit_company")
        self.gridLayout.addWidget(self.lineedit_company, 2, 3, 1, 1)

        self.label_email_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_email_1.setFont(font)
        self.label_email_1.setObjectName("label_email_1")
        self.gridLayout.addWidget(self.label_email_1, 3, 4, 1, 1)

        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.add_button.setFont(font)
        self.add_button.setObjectName("add_button")
        self.gridLayout.addWidget(self.add_button, 0, 7, 1, 1)

        self.label_lname = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_lname.setFont(font)
        self.label_lname.setObjectName("label_lname")
        self.gridLayout.addWidget(self.label_lname, 1, 2, 1, 1)

        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setMinimumSize(QtCore.QSize(0, 40))
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 1, 7, 1, 1)

        self.lineedit_phone_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_phone_1.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_phone_1.setFont(font)
        self.lineedit_phone_1.setObjectName("lineedit_phone_1")
        self.gridLayout.addWidget(self.lineedit_phone_1, 0, 5, 1, 1)

        self.lineedit_phone_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_phone_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_phone_2.setFont(font)
        self.lineedit_phone_2.setObjectName("lineedit_phone_2")
        self.gridLayout.addWidget(self.lineedit_phone_2, 1, 5, 1, 1)

        self.lineedit_fname = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineedit_fname.sizePolicy().hasHeightForWidth()
        )

        self.lineedit_fname.setSizePolicy(sizePolicy)
        self.lineedit_fname.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_fname.setFont(font)
        self.lineedit_fname.setObjectName("lineedit_fname")
        self.gridLayout.addWidget(self.lineedit_fname, 0, 3, 1, 1)

        self.outlook_button = QtWidgets.QPushButton(self.centralwidget)
        self.outlook_button.setMinimumSize(QtCore.QSize(0, 40))
        self.outlook_button.setObjectName("outlook_button")
        self.gridLayout.addWidget(self.outlook_button, 2, 7, 1, 1)

        self.label_job_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_job_title.setFont(font)
        self.label_job_title.setObjectName("label_job_title")
        self.gridLayout.addWidget(self.label_job_title, 3, 2, 1, 1)

        self.lineedit_job_title = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_job_title.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_job_title.setFont(font)
        self.lineedit_job_title.setObjectName("lineedit_job_title")
        self.gridLayout.addWidget(self.lineedit_job_title, 3, 3, 1, 1)

        self.lineedit_email_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_email_1.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_email_1.setFont(font)
        self.lineedit_email_1.setObjectName("lineedit_email_1")
        self.gridLayout.addWidget(self.lineedit_email_1, 3, 5, 1, 1)

        self.cb_email_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_email_1.setText("")
        self.cb_email_1.setObjectName("cb_email_1")
        self.gridLayout.addWidget(self.cb_email_1, 3, 6, 1, 1)

        self.cb_phone_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_phone_1.setText("")
        self.cb_phone_1.setObjectName("cb_phone_1")
        self.gridLayout.addWidget(self.cb_phone_1, 0, 6, 1, 1)

        self.date_button = QtWidgets.QPushButton(self.centralwidget)
        self.date_button.setMinimumSize(QtCore.QSize(0, 40))
        self.date_button.setObjectName("date_button")
        self.gridLayout.addWidget(self.date_button, 3, 7, 1, 1)

        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setMinimumSize(QtCore.QSize(0, 40))
        self.delete_button.setObjectName("date_button")
        self.gridLayout.addWidget(self.delete_button, 4, 7, 1, 1)

        self.label_category = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_category.setFont(font)
        self.label_category.setObjectName("label_category")
        self.gridLayout.addWidget(self.label_category, 4, 2, 1, 1)

        self.cb_phone_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_phone_3.setText("")
        self.cb_phone_3.setObjectName("cb_phone_3")
        self.gridLayout.addWidget(self.cb_phone_3, 2, 6, 1, 1)

        self.label_search = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_search.setFont(font)
        self.label_search.setObjectName("label_search")
        self.gridLayout.addWidget(self.label_search, 0, 0, 1, 1)

        self.lineedit_search = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_search.setFont(font)
        self.lineedit_search.setObjectName("lineedit_search")
        self.gridLayout.addWidget(self.lineedit_search, 0, 1, 1, 1)

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setMinimumSize(QtCore.QSize(515, 400))
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.table, 1, 0, 15, 2)

        self.notes_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.notes_text_edit.sizePolicy().hasHeightForWidth()
        )

        self.notes_text_edit.setSizePolicy(sizePolicy)
        self.notes_text_edit.setMinimumSize(QtCore.QSize(400, 50))
        self.notes_text_edit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.notes_text_edit.setFont(font)
        self.notes_text_edit.setObjectName("notes_text_edit")
        self.gridLayout.addWidget(self.notes_text_edit, 8, 2, 1, 6)

        self.cb_email_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_email_2.setText("")
        self.cb_email_2.setObjectName("cb_email_2")
        self.gridLayout.addWidget(self.cb_email_2, 4, 6, 1, 1)

        self.label_notes = QtWidgets.QLabel(self.centralwidget)
        self.label_notes.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_notes.sizePolicy().hasHeightForWidth())
        self.label_notes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_notes.setFont(font)
        self.label_notes.setObjectName("label_notes")
        self.gridLayout.addWidget(self.label_notes, 7, 2, 1, 1)

        self.label_email_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_email_2.setFont(font)
        self.label_email_2.setObjectName("label_email_2")
        self.gridLayout.addWidget(self.label_email_2, 4, 4, 1, 1)

        self.lineedit_email_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_email_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineedit_email_2.setFont(font)
        self.lineedit_email_2.setObjectName("lineedit_email_2")
        self.gridLayout.addWidget(self.lineedit_email_2, 4, 5, 1, 1)

        self.label_fname = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_fname.setFont(font)
        self.label_fname.setObjectName("label_fname")
        self.gridLayout.addWidget(self.label_fname, 0, 2, 1, 1)

        self.email_view = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_view.sizePolicy().hasHeightForWidth())
        self.email_view.setSizePolicy(sizePolicy)
        self.email_view.setObjectName("widget")
        self.gridLayout.addWidget(self.email_view, 10, 2, 6, 6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionAdd_New_Contact = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Contact.setObjectName("actionAdd_New_Contact")
        self.actionAdd_New_Category = QtWidgets.QAction(MainWindow)
        self.actionAdd_New_Category.setObjectName("actionAdd_New_Category")
        self.actionDelete_Category_List = QtWidgets.QAction(MainWindow)
        self.actionDelete_Category_List.setObjectName("actionDelete_Category_List")
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionDark_Mode = QtWidgets.QAction(MainWindow)
        self.actionDark_Mode.setObjectName("actionDark_Mode")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEdit_Current_Contact = QtWidgets.QAction(MainWindow)
        self.actionEdit_Current_Contact.setObjectName("actionEdit_Current_Contact")
        self.actionDelete_category = QtWidgets.QAction(MainWindow)
        self.actionDelete_category.setObjectName("aactionDelete_category")
        self.actionView_Stretch = QtWidgets.QAction(MainWindow)
        self.actionView_Stretch.setObjectName("actionView_Stretch")
        self.actionView_Interactive = QtWidgets.QAction(MainWindow)
        self.actionView_Interactive.setObjectName("actionView_Interactive")
        self.actionView_Fixed = QtWidgets.QAction(MainWindow)
        self.actionView_Fixed.setObjectName("actionView_Fixed")
        self.actionView_ResizeToContents = QtWidgets.QAction(MainWindow)
        self.actionView_ResizeToContents.setObjectName("actionView_ResizeToContents")

        self.menuFile.addAction(self.actionAdd_New_Contact)
        self.menuFile.addAction(self.actionAdd_New_Category)
        self.menuFile.addAction(self.actionDelete_Category_List)
        self.menuEdit.addAction(self.actionEdit_Current_Contact)
        self.menuEdit.addAction(self.actionDelete_category)
        self.menuView.addAction(self.actionView_Stretch)
        self.menuView.addAction(self.actionView_Interactive)
        self.menuView.addAction(self.actionView_Fixed)
        self.menuView.addAction(self.actionView_ResizeToContents)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineedit_search, self.lineedit_fname)
        MainWindow.setTabOrder(self.lineedit_fname, self.lineedit_lname)
        MainWindow.setTabOrder(self.lineedit_lname, self.lineedit_company)
        MainWindow.setTabOrder(self.lineedit_company, self.lineedit_job_title)
        MainWindow.setTabOrder(self.lineedit_job_title, self.lineedit_street_line_1)
        # category may go here if it is a field
        MainWindow.setTabOrder(self.lineedit_street_line_1, self.lineedit_street_line_2)
        MainWindow.setTabOrder(self.lineedit_street_line_2, self.lineedit_phone_1)
        MainWindow.setTabOrder(self.lineedit_phone_1, self.lineedit_phone_2)
        MainWindow.setTabOrder(self.lineedit_phone_2, self.lineedit_phone_3)
        MainWindow.setTabOrder(self.lineedit_phone_3, self.lineedit_email_1)
        MainWindow.setTabOrder(self.lineedit_email_1, self.lineedit_email_2)
        MainWindow.setTabOrder(self.lineedit_email_2, self.lineedit_city)
        MainWindow.setTabOrder(self.lineedit_city, self.lineedit_state)
        MainWindow.setTabOrder(self.lineedit_state, self.lineedit_zip)
        MainWindow.setTabOrder(self.lineedit_zip, self.notes_text_edit)

        # Globals within class
        self.darkmode = False
        self.currentContact = None
        self.addMode = False
        self.editMode = False
        self.view_expanded = False
        self.resizemode = "Stretch"

        # Filling table
        self.updateTable()
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.setSortingEnabled(True)
        self.table.cellClicked.connect(self.cell_clicked)

        # Setting Qcompleter
        model_search = QtCore.QStringListModel()
        model_search.setStringList(set_Qcompleter())
        completer = QtWidgets.QCompleter()
        completer.setModel(model_search)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.lineedit_search.setCompleter(completer)

        # Binding Qcompleter to the dynamic table
        self.lineedit_search.textEdited.connect(self.search_changed)

        # Add QAction and QPushButton functionality
        self.actionAdd_New_Contact.triggered.connect(self.add_contact)
        self.actionAdd_New_Category.triggered.connect(self.add_new_category)
        self.actionDelete_Category_List.triggered.connect(self.delete_category_list)
        self.add_button.clicked.connect(self.add_new_contact)
        self.actionView_Stretch.triggered.connect(self.change_view_Stretch)
        self.actionView_Interactive.triggered.connect(self.change_view_Interactive)
        self.actionView_Fixed.triggered.connect(self.change_view_Fixed)
        self.actionView_ResizeToContents.triggered.connect(
            self.change_view_ResizeToContents
        )
        self.actionEdit_Current_Contact.triggered.connect(self.edit_contact)
        self.actionDelete_category.triggered.connect(self.delete_category_from_contact)
        self.save_button.clicked.connect(self.edit_current_contact)
        self.delete_button.clicked.connect(self.delete_contact)

        # Set Outlook QPushbutton
        self.outlook_button.clicked.connect(self.open_outlook)

        # Set DateStamp Button
        self.date_button.clicked.connect(self.set_datestamp)
        self.set_lineEdits_ReadOnly()
        self.lineedit_search.setFocus()

    def add_contact(self):
        self.clear_lineedits()
        self.editMode = False
        self.addMode = True
        self.set_lineEdits_Writeable()
        self.lineedit_fname.setFocus()
        self.currentContact = None
        self.change_lineedits_add(True)

    def add_new_category(self):
        categories = get_all_categories()
        input_dialog = Input_Dialog()
        similarity = [0, 0]
        if input_dialog.text is not None:
            for i in categories:
                x = difflib.SequenceMatcher(None, input_dialog.text, i).ratio()
                if x > similarity[0]:
                    similarity[0] = x
                    similarity[1] = i
            similarity[0] = str(similarity[0] * 100)[0:4]
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText(
                "The most similar existing category is "
                + similarity[1]
                + "("
                + similarity[0]
                + "% match) \n Do you want to proceed?"
            )
            msgBox.setWindowTitle("Duplicate Check")
            msgBox.setStandardButtons(
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
            )
            buttonReply = msgBox.exec()
            if buttonReply == QtWidgets.QMessageBox.Yes:
                result = new_main_category(input_dialog.selection)
                if result == "update":
                    self.show_dialog(result)
                else:
                    self.show_dialog("query")

    def add_new_contact(self):
        if self.addMode == True:
            self.set_lineEdits_ReadOnly()
            query_list = [
                self.lineedit_fname.text(),
                self.lineedit_lname.text(),
                self.lineedit_company.text(),
                self.lineedit_job_title.text(),
                self.lineedit_email_1.text(),
                self.lineedit_email_2.text(),
                "",
                self.fix_phone_numbers(self.lineedit_phone_1.text(), False),
                self.fix_phone_numbers(self.lineedit_phone_1.text(), False),
                self.fix_phone_numbers(self.lineedit_phone_1.text(), False),
                self.lineedit_street_line_1.text(),
                self.lineedit_street_line_2.text(),
                self.lineedit_city.text(),
                self.lineedit_state.text(),
                self.lineedit_zip.text(),
                self.notes_text_edit.toPlainText(),
            ]

            exists = exists_query(query_list)
            if exists == False:
                self.addMode = True
                result = insert_contact(query_list)
                if result == "add":
                    self.show_dialog("add")
                    self.change_lineedits_add(False)
                    self.updateTable()
                    self.clear_lineedits()
                else:
                    self.show_dialog("query")
            else:
                self.show_dialog("duplicate")
            self.addMode = False
            self.change_lineedits_add(False)
        else:
            self.show_dialog("addmode")

    def cell_clicked(self, row):
        self.editMode = False
        self.addMode = False
        self.change_lineedits_add(False)
        self.clear_lineedits()
        name = self.table.item(row, 0).text()
        company = self.table.item(row, 1).text()
        phone = self.fix_phone_numbers(self.table.item(row, 2).text(), False)
        email = self.table.item(row, 3).text()
        category = self.table.item(row, 4).text()
        names = name.split()
        if len(names) == 2:
            fname, lname = names[0], names[1]
        elif len(names) == 1:
            fname = names[0]
            lname = ""
        else:
            fname, lname = "", ""
        my_list = [fname, lname, company, phone, email, category]
        contact = query_one_contact(my_list)
        self.currentContact = contact[0]
        self.set_lineedits(contact)
        self.set_boxes()
        self.lineedit_search.setReadOnly(False)
        self.load_categories(category)
        self.set_email_window(contact[5])

    def change_lineedits_add(self, isTrue):
        if isTrue == True:
            self.lineedit_fname.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_lname.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_company.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_job_title.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_phone_1.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_phone_2.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_phone_3.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_email_1.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_email_2.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_street_line_1.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_street_line_2.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_city.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_state.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.lineedit_zip.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
            self.notes_text_edit.setStyleSheet(
                "QLineEdit { background-color: #AE6767; color: black }"
            )
        else:
            self.lineedit_fname.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_lname.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_company.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_job_title.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_phone_1.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_phone_2.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_phone_3.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_email_1.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_email_2.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_street_line_1.setStyleSheet(
                "QLineEdit { background-color#FFFFFF; color: black }"
            )
            self.lineedit_street_line_2.setStyleSheet(
                "QLineEdit { background-color#FFFFFF; color: black }"
            )
            self.lineedit_city.setStyleSheet(
                "QLineEdit { background-color#FFFFFF; color: black }"
            )
            self.lineedit_state.setStyleSheet(
                "QLineEdit { background-color#FFFFFF; color: black }"
            )
            self.lineedit_zip.setStyleSheet(
                "QLineEdit { background-color#FFFFFF; color: black }"
            )
            # self.lineedit_category.setStyleSheet( "QLineEdit { background-color :#FFFFFF; color: black }")
            self.notes_text_edit.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )

    def change_lineedits_edit(self, isTrue):
        if isTrue == True:
            self.lineedit_fname.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_lname.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_company.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_job_title.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_phone_1.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_phone_2.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_phone_3.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_email_1.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_email_2.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_street_line_1.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_street_line_2.setStyleSheet(
                "QLineEdit { background-color:#80FF00; color: black }"
            )
            self.lineedit_city.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_state.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.lineedit_zip.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
            self.notes_text_edit.setStyleSheet(
                "QLineEdit { background-color: #80FF00; color: black }"
            )
        else:
            self.lineedit_fname.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_lname.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_company.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_job_title.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_phone_1.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_phone_2.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_phone_3.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_email_1.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_email_2.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_street_line_1.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_street_line_2.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_city.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_state.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.lineedit_zip.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )
            self.notes_text_edit.setStyleSheet(
                "QLineEdit { background-color: #FFFFFF; color: black }"
            )

    def change_view_Fixed(self):
        self.resizemode = "Fixed"
        self.updateTable()

    def change_view_Interactive(self):
        self.resizemode = "Interactive"
        self.updateTable()

    def change_view_ResizeToContents(self):
        self.resizemode = "ResizeToContents"
        self.updateTable()

    def change_view_Stretch(self):
        self.resizemode = "ResizeToContents"
        self.updateTable()

    def check_box_status(self):
        contact_info = [
            self.cb_phone_1.isChecked(),
            self.cb_phone_2.isChecked(),
            self.cb_phone_3.isChecked(),
            self.cb_email_1.isChecked(),
            self.cb_email_2.isChecked(),
        ]
        c = update_last_known(str(contact_info), self.currentContact)

    def clear_lineedits(self):
        self.lineedit_fname.setText("")
        self.lineedit_lname.setText("")
        self.lineedit_company.setText("")
        self.lineedit_job_title.setText("")
        self.lineedit_phone_1.setText("")
        self.lineedit_phone_2.setText("")
        self.lineedit_phone_3.setText("")
        self.lineedit_email_1.setText("")
        self.lineedit_email_2.setText("")
        self.lineedit_street_line_1.setText("")
        self.lineedit_street_line_2.setText("")
        self.lineedit_city.setText("")
        self.lineedit_state.setText("")
        self.lineedit_zip.setText("")
        self.notes_text_edit.setText("")

    def combo(self):
        selected = self.category_combobox.currentText()
        if selected == "Add client to existing category":
            dialog = Combo_Dialog(None)
            if dialog.selection != None:
                updated = update_category(self.currentContact, dialog.selection)
                self.load_categories(updated)
                self.updateTable()
            else:
                pass

    def delete_contact(self):
        self.editMode = False
        if self.currentContact == None:
            self.show_dialog("none")
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText(
                "Are you sure you want to delete this contact? This action cannot be reversed."
            )
            msgBox.setWindowTitle("Delete Prompt")
            msgBox.setStandardButtons(
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
            )
            buttonReply = msgBox.exec()

            if buttonReply == QtWidgets.QMessageBox.Yes:
                result = delete_from_id(self.currentContact)
                if result == True:
                    self.show_dialog("error_delete")
                else:
                    self.show_dialog("delete")
                    self.clear_lineedits()
                    self.updateTable()
                    self.change_lineedits_edit(False)
                    self.set_lineEdits_ReadOnly()
            if buttonReply == QtWidgets.QMessageBox.Cancel:
                pass

    def delete_category_list(self):
        dialog = Category_Dialog()
        selection = dialog.selection
        if selection is not None:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Information)
            msgBox.setText(
                "Are you sure you want to delete this category? This action cannot be reversed."
            )
            msgBox.setWindowTitle("Delete Prompt")
            msgBox.setStandardButtons(
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel
            )
            buttonReply = msgBox.exec()
            if buttonReply == QtWidgets.QMessageBox.Yes:
                result = delete_category(selection)
                if result == "update":
                    self.show_dialog(result)
                else:
                    self.show_dialog("query")
            if buttonReply == QtWidgets.QMessageBox.Cancel:
                pass
        else:
            pass

    def delete_category_from_contact(self):
        if self.currentContact != None:
            result = query_one_contact(None, self.currentContact)
            if result is not None:
                dialog = Combo_Dialog(self.currentContact)
                if dialog.selection != None:
                    updated = update_category(
                        self.currentContact, dialog.selection, delete=True
                    )
                    self.load_categories(updated)
                    self.updateTable()
            else:
                self.show_dialog("error_delete")
        else:
            self.show_dialog("none")

    def edit_contact(self):
        if self.currentContact != None:
            self.editMode = True
            self.addMode = False
            self.set_lineEdits_Writeable()
            self.change_lineedits_edit(True)
        else:
            self.show_dialog("none")

    def edit_current_contact(self):
        if self.editMode == True:
            self.set_lineEdits_ReadOnly()
            query_list = [
                self.lineedit_fname.text(),
                self.lineedit_lname.text(),
                self.lineedit_company.text(),
                self.lineedit_job_title.text(),
                self.lineedit_email_1.text(),
                self.lineedit_email_2.text(),
                "",
                self.fix_phone_numbers(self.lineedit_phone_1.text(), False),
                self.fix_phone_numbers(self.lineedit_phone_2.text(), False),
                self.fix_phone_numbers(self.lineedit_phone_3.text(), False),
                self.lineedit_street_line_1.text(),
                self.lineedit_street_line_2.text(),
                self.lineedit_city.text(),
                self.lineedit_state.text(),
                self.lineedit_zip.text(),
                self.notes_text_edit.toPlainText(),
            ]
            result = update_contact(query_list, self.currentContact)
            self.check_box_status()
            if result == "update":
                self.show_dialog("update")
                self.updateTable()
                self.editMode = False
                self.change_lineedits_edit(False)
            else:
                self.show_dialog("query")
            self.editMode = False
        else:
            self.show_dialog("none")

    def fix_phone_numbers(self, phone, display):
        if phone != None and phone != "":
            if display:
                return phone[0:3] + "-" + phone[3:6] + "-" + phone[6:]
            else:
                p = phone
                p = p.replace("-", "")
                p = p.replace("(", "")
                p = p.replace(")", "")
                p = p.replace("", "")
                return p
        else:
            return ""

    def load_categories(self, categories):
        self.category_combobox.clear()
        for i in categories.split(";"):
            if i == "":
                self.category_combobox.addItem("Client is not in any category")
                self.category_combobox.addItem("Add client to existing category")
                return
            else:
                self.category_combobox.addItem(i)
        self.category_combobox.addItem("Add client to existing category")

    def open_outlook(self):
        if self.lineedit_email_1.text() != "":
            outlook = Dispatch("Outlook.Application")
            mail = outlook.CreateItem(0)
            if self.lineedit_email_1.text() != "":
                email_list = self.lineedit_email_1.text().split(" ")
                for i in email_list:
                    if "@" in i:
                        mail.To = i
                        break
                mail.Display(True)
            else:
                self.show_dialog("outlook")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CRM"))
        self.label_email_history.setText(_translate("MainWindow", "Email History:"))
        self.label_phone_1.setText(_translate("MainWindow", "Bus. Phone:"))
        self.label_company.setText(_translate("MainWindow", "Company:"))
        self.label_phone_2.setText(_translate("MainWindow", "Bus. Phone 2:"))
        self.label_phone_3.setText(_translate("MainWindow", "Mobile Phone:"))
        self.label_email_1.setText(_translate("MainWindow", "Bus. Email:"))
        self.add_button.setText(_translate("MainWindow", "Add Contact"))
        self.label_lname.setText(_translate("MainWindow", "Last Name:"))
        self.save_button.setText(_translate("MainWindow", "Save Contact"))
        self.outlook_button.setText(_translate("MainWindow", "Open w/Outlook"))
        self.label_job_title.setText(_translate("MainWindow", "Job Title:"))
        self.date_button.setText(_translate("MainWindow", "Date Stamp"))
        self.label_category.setText(_translate("MainWindow", "Category:"))
        self.label_search.setText(_translate("MainWindow", "Search:"))
        self.label_street_line_1.setText(_translate("Mainwindow", "Street Line 1:"))
        self.label_street_line_2.setText(_translate("Mainwindow", "Street Line 2:"))
        self.label_city.setText(_translate("Mainwindow", "City:"))
        self.label_state.setText(_translate("Mainwindow", "State:"))
        self.label_zip.setText(_translate("Mainwindow", "Zip:"))
        self.delete_button.setText(_translate("Mainwindow", "Delete Contact"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Company"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Category"))
        self.label_notes.setText(_translate("MainWindow", "Notes:"))
        self.label_email_2.setText(_translate("MainWindow", "Pers. Email:"))
        self.label_fname.setText(_translate("MainWindow", "First Name:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionAdd_New_Contact.setText(_translate("MainWindow", "Add New Contact"))
        self.actionAdd_New_Category.setText(
            _translate("Mainwindow", "Add New Category")
        )
        self.actionDelete_Category_List.setText(
            _translate("Mainwindow", "Delete Existing Category")
        )
        self.actionEdit_Current_Contact.setText(
            _translate("MainWindow", "Edit Current Contact")
        )
        self.actionDelete_category.setText(
            _translate("MainWindow", "Delete Category From Contact")
        )
        self.actionView_Stretch.setText(_translate("MainWindow", "Stretch"))
        self.actionView_Interactive.setText(_translate("MainWindow", "Interactive"))
        self.actionView_Fixed.setText(_translate("MainWindow", "Fixed"))
        self.actionView_ResizeToContents.setText(
            _translate("MainWindow", "Resize To Contents")
        )

    def search_changed(self):
        search = self.lineedit_search.text()
        if search == "":
            self.updateTable()
        elif " " in search:
            try:
                search = stringify(search)
                results = search_space_query(search)
                self.temp_table(results)
            except:
                self.table.setRowCount(0)
        else:
            try:
                search = "'%" + str(search) + "%'"
                results = search_query(search)
                self.temp_table(results)
            except:
                self.table.setRowCount(0)

    def set_boxes(self):
        self.cb_phone_1.setChecked(False)
        self.cb_phone_2.setChecked(False)
        self.cb_phone_3.setChecked(False)
        self.cb_email_1.setChecked(False)
        self.cb_email_2.setChecked(False)
        boxes = query_last_known(self.currentContact)
        boxes = ast.literal_eval(boxes)
        if boxes[0] == True:
            self.cb_phone_1.setChecked(True)
        if boxes[1] == True:
            self.cb_phone_1.setChecked(True)
        if boxes[2] == True:
            self.cb_phone_1.setChecked(True)
        if boxes[3] == True:
            self.cb_email_1.setChecked(True)
        if boxes[4] == True:
            self.cb_email_2.setChecked(True)

    def set_datestamp(self):
        now = datetime.datetime.now()
        dt_string = now.strftime("%m/%d/%Y|%I:%M") + "|Tim- "
        pyperclip.copy(dt_string)

    def set_email_window(self, email):
        body = query_email(email)
        self.email_view.setHtml(body)

    def set_lineedits(self, contact):
        self.lineedit_fname.setText(contact[1])
        self.lineedit_lname.setText(contact[2])
        self.lineedit_company.setText(contact[3])
        self.lineedit_job_title.setText(contact[4])
        self.lineedit_phone_1.setText(self.fix_phone_numbers(contact[8], True))
        self.lineedit_phone_2.setText(self.fix_phone_numbers(contact[9], True))
        self.lineedit_phone_3.setText(self.fix_phone_numbers(contact[10], True))
        self.lineedit_email_1.setText(contact[5])
        self.lineedit_email_2.setText(contact[6])
        self.lineedit_street_line_1.setText(contact[11])
        self.lineedit_street_line_2.setText(contact[12])
        self.lineedit_city.setText(contact[13])
        self.lineedit_state.setText(contact[14])
        self.lineedit_zip.setText(contact[15])
        self.notes_text_edit.setText(contact[16])
        self.set_lineEdits_ReadOnly()

    def set_lineEdits_ReadOnly(self):
        self.lineedit_fname.setReadOnly(True)
        self.lineedit_lname.setReadOnly(True)
        self.lineedit_company.setReadOnly(True)
        self.lineedit_job_title.setReadOnly(True)
        self.lineedit_phone_1.setReadOnly(True)
        self.lineedit_phone_2.setReadOnly(True)
        self.lineedit_phone_3.setReadOnly(True)
        self.lineedit_email_1.setReadOnly(True)
        self.lineedit_email_2.setReadOnly(True)
        self.lineedit_street_line_1.setReadOnly(True)
        self.lineedit_street_line_2.setReadOnly(True)
        self.lineedit_city.setReadOnly(True)
        self.lineedit_state.setReadOnly(True)
        self.lineedit_zip.setReadOnly(True)
        self.notes_text_edit.setReadOnly(True)

    def set_lineEdits_Writeable(self):
        self.lineedit_fname.setReadOnly(False)
        self.lineedit_lname.setReadOnly(False)
        self.lineedit_company.setReadOnly(False)
        self.lineedit_job_title.setReadOnly(False)
        self.lineedit_phone_1.setReadOnly(False)
        self.lineedit_phone_2.setReadOnly(False)
        self.lineedit_phone_3.setReadOnly(False)
        self.lineedit_email_1.setReadOnly(False)
        self.lineedit_email_2.setReadOnly(False)
        self.lineedit_street_line_1.setReadOnly(False)
        self.lineedit_street_line_2.setReadOnly(False)
        self.lineedit_city.setReadOnly(False)
        self.lineedit_state.setReadOnly(False)
        self.lineedit_zip.setReadOnly(False)
        self.notes_text_edit.setReadOnly(False)

    def show_dialog(self, sender, id=None):
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("Alert!")
        if sender == "outlook":
            message.setText("Email field is empty")
        elif sender == "query":
            message.setText("Cant' receive from DB")
        elif sender == "add":
            message.setWindowTitle("Success!")
            message.setText("Successfully added to DB")
        elif sender == "duplicate":
            message.setText("Dup. found in DB or not enough info")
        elif sender == "edit":
            message.setText('Click "Edit" to make changes')
        elif sender == "addmode":
            message.setText('Click "File" to add new contact')
        elif sender == "update":
            message.setWindowTitle("Success!")
            message.setText("Database updated successfully")
        elif sender == "same":
            message.setWindowTitle("Oops!")
            message.setText("Data looks the same or error from DB")
        elif sender == "none":
            message.setWindowTitle("Oops!")
            message.setText("No contact currently selected")
        elif sender == "error_delete":
            message.setWindowTitle("Alert!")
            message.setText("Error removing from DB")
        elif sender == "delete":
            message.setWindowTitle("Success!")
            message.setText("Contact removed from DB")
        message.exec()

    def temp_table(self, results):
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Name", "Company", "Phone 1 ", "Email 1", "Category"]
        )
        results = make_names(results)
        self.table.setRowCount(len(results))
        header = self.table.horizontalHeader()
        for i in range(len(results)):
            results[i][2] = self.fix_phone_numbers(results[i][2], True)
        for i in range(len(results)):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(results[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(results[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(results[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(results[i][3]))
            self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(results[i][4]))
        if self.resizemode == "Stretch":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        if self.resizemode == "Interactive":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Interactive)
        if self.resizemode == "Fixed":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        if self.resizemode == "ResizeToContents":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)

    def updateTable(self):
        self.table.setRowCount(0)
        contacts = query_all_contacts()
        length = 0
        contacts = []
        for i in range(len(contacts)):
            contacts[i][2] = self.fix_phone_numbers(contacts[i][2], True)
        self.table.setColumnCount(5)
        self.table.setRowCount(length)
        self.table.setHorizontalHeaderLabels(
            ["Name", "Company", "Phone 1 ", "Email 1", "Category"]
        )
        header = self.table.horizontalHeader()
        for i in range(len(contacts)):
            self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(contacts[i][0]))
            self.table.setItem(i, 1, QtWidgets.QTableWidgetItem(contacts[i][1]))
            self.table.setItem(i, 2, QtWidgets.QTableWidgetItem(contacts[i][2]))
            self.table.setItem(i, 3, QtWidgets.QTableWidgetItem(contacts[i][3]))
            self.table.setItem(i, 4, QtWidgets.QTableWidgetItem(contacts[i][4]))
        if self.resizemode == "Stretch":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        if self.resizemode == "Interactive":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Interactive)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Interactive)
        if self.resizemode == "Fixed":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.Fixed)
        if self.resizemode == "ResizeToContents":
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
