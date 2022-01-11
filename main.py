from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QWidget, QErrorMessage, QFileDialog
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from Py_Interface_files.Main_interface import Ui_MainWindow
from Py_Interface_files.Dialog_note_edit import Ui_Dialog as Ui_TaksEdit
from Py_Interface_files.Dialog_date_edit import Ui_Dialog as Ui_DateEdit

import os
import io
import sys
import csv

import CSVManager
import SysFilesManager

class TaskEdit(QDialog, Ui_TaksEdit): #диалоговое окно редактирования задания
    def __init__(self, parent=None):
        super(TaskEdit, self).__init__()
        self.ui = Ui_TaksEdit()
        self.ui.setupUi(self)

        self.Data = []

        self.ui.btn_ok.clicked.connect(self.okClicked)
        self.ui.btn_cancel.clicked.connect(self.cancelClicked)

    def okClicked(self):
        self.Data.clear()
        self.Data.append(self.ui.edit_Date.date().toString("dd.MM.yyyy"))
        self.Data.append(self.ui.edit_Time.time().toString())
        self.Data.append(self.ui.edit_Short.text())
        self.Data.append(self.ui.edit_Full.toPlainText())
        self.close()

    def cancelClicked(self):
        self.Data = None
        self.close()


class Window(QMainWindow, Ui_MainWindow): #основное окно
    def __init__(self, parent=None):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.model = QStandardItemModel()
        self.ui.model.setHorizontalHeaderLabels(['Дата', 'Время', 'Название', 'Описание'])
        self.ui.tableView.setModel(self.ui.model)
        self.ui.tableView.setEnabled(False)

        self.ui.create.triggered.connect(self.createClicked)
        self.ui.save.triggered.connect(self.saveClicked)
        self.ui.saveAs.triggered.connect(self.saveAsClicked)
        self.ui.open.triggered.connect(self.loadClicked)
        self.ui.add.triggered.connect(self.addClicked)

    def createClicked(self):
        if SysFilesManager.file_saved:
            CSVManager.createCSV()
            CSVManager.returnModel(True)
            self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Tasks - temp*"))
        else:
            reply = QMessageBox.question(self, 'Creation', "Вы уверенны, что хотите создать новый файл?\nНесохранённые изменения будут утеряны.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                CSVManager.createCSV()
                CSVManager.returnModel(True)
                self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Tasks - temp*"))
            else:
                pass

    def addClicked(self):
        dialog = TaskEdit()
        dialog.show()
        dialog.exec_()
        if dialog.Data is not None:
            CSVManager.addCSV(dialog.Data)
            self.ui.model = CSVManager.returnModel(False)
            self.ui.tableView.setModel(self.ui.model)
            self.ui.tableView.update()
            self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {SysFilesManager.config['Last_file'].split('/')[-1]}*"))

    def loadClicked(self):
        path = QFileDialog.getOpenFileName(self, 'Save File', filter="Tables (*.csv)", directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        CSVManager.copyCSV(path[0])
        self.ui.model = CSVManager.returnModel(False)
        self.ui.tableView.setModel(self.ui.model)
        self.ui.tableView.update()
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {path[0].split('/')[-1]}"))

    def saveClicked(self):
        if SysFilesManager.config["Last_file"] == "None":
            path = QFileDialog.getSaveFileName(self, 'Save File', filter="Tables (*.csv)", directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
            SysFilesManager.config["Last_file"] = path[0]
            CSVManager.saveCSV(path[0])
        else:
            CSVManager.saveCSV(SysFilesManager.config["Last_file"])
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {SysFilesManager.config['Last_file'].split('/')[-1]}"))


    def saveAsClicked(self):
        path = QFileDialog.getSaveFileName(self, 'Save File', filter="Tables (*.csv)", directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        SysFilesManager.config["Last_file"] = path[0]
        CSVManager.saveCSV(path[0])
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {SysFilesManager.config['Last_file'].split('/')[-1]}"))


if __name__ == "__main__":
    SysFilesManager.check()

    app = QApplication([])
    application = Window()
    application.show()
    SysFilesManager.initialization()

    sys.exit(app.exec())
