# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 198)
        self.center = QtWidgets.QWidget(MainWindow)
        self.center.setObjectName("center")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.center)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tableView = QtWidgets.QTableView(self.center)
        self.tableView.setObjectName("tableView")

        self.verticalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.center)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.file_menu = QtWidgets.QMenu(self.menubar)
        self.file_menu.setObjectName("file_menu")
        self.creators = QtWidgets.QMenu(self.menubar)
        self.creators.setObjectName("creators")
        self.action_menu = QtWidgets.QMenu(self.menubar)
        self.action_menu.setObjectName("action_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.save = QtWidgets.QAction(MainWindow)
        self.save.setObjectName("save")
        self.create = QtWidgets.QAction(MainWindow)
        self.create.setObjectName("create")
        self.open = QtWidgets.QAction(MainWindow)
        self.open.setObjectName("open")
        self.add = QtWidgets.QAction(MainWindow)
        self.add.setObjectName("add")
        self.remove = QtWidgets.QAction(MainWindow)
        self.remove.setObjectName("remove")
        self.saveAs = QtWidgets.QAction(MainWindow)
        self.saveAs.setObjectName("saveAs")
        self.file_menu.addAction(self.create)
        self.file_menu.addAction(self.saveAs)
        self.file_menu.addAction(self.save)
        self.file_menu.addAction(self.open)
        self.action_menu.addAction(self.add)
        self.action_menu.addAction(self.remove)
        self.menubar.addAction(self.file_menu.menuAction())
        self.menubar.addAction(self.action_menu.menuAction())
        self.menubar.addAction(self.creators.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tasks"))
        self.file_menu.setTitle(_translate("MainWindow", "Файл"))
        self.creators.setTitle(_translate("MainWindow", "Создатели"))
        self.action_menu.setTitle(_translate("MainWindow", "Действия"))
        self.save.setText(_translate("MainWindow", "Сохранить"))
        self.save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.create.setText(_translate("MainWindow", "Создать"))
        self.create.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.open.setText(_translate("MainWindow", "Открыть"))
        self.open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.add.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.remove.setText(_translate("MainWindow", "Удалить"))
        self.remove.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.saveAs.setText(_translate("MainWindow", "Сохранить как"))
