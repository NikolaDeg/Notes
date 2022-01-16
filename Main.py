from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QStandardItemModel

from Py_Interface_files.Main_interface import Ui_MainWindow
from Py_Interface_files.Dialog_note_edit import Ui_Dialog as Ui_TaksEdit

import os
import sys

from File_Managers import CSVManager, SysFilesManager


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
        self.ui.model.setHorizontalHeaderLabels(['Date', 'Time', 'Name', 'Description'])
        self.ui.tableView.setModel(self.ui.model)
        self.ui.tableView.setEnabled(False)

        self.ui.create.triggered.connect(self.create_clicked)
        self.ui.save.triggered.connect(self.save_clicked)
        self.ui.saveAs.triggered.connect(self.save_as_clicked)
        self.ui.open.triggered.connect(self.load_clicked)
        self.ui.add.triggered.connect(self.add_clicked)

    def create_clicked(self):
        if SysFilesManager.file_saved:
            CSVManager.create_csv()
            CSVManager.return_model(True)
            self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Tasks - temp*"))
        else:
            reply = QMessageBox.question(self, 'Creation', "Are you sure you want to create a new file?\nUnsaved changes will be lost", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                CSVManager.create_csv()
                CSVManager.return_model(True)
                self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Tasks - temp*"))
            else:
                pass

    # Event method
    def add_clicked(self):
        dialog = TaskEdit()
        dialog.show()
        dialog.exec_()
        if dialog.Data is not None:
            CSVManager.add_csv(dialog.Data)
            self.ui.model = CSVManager.return_model(False)
            self.ui.tableView.setModel(self.ui.model)
            self.ui.tableView.update()
            if not SysFilesManager.config["Last_file"] == "None":
                self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {SysFilesManager.config['Last_file'].split('/')[-1]}*"))
            else:
                self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", "Tasks - temp*"))

    # Event method
    def load_clicked(self):
        path = QFileDialog.getOpenFileName(self, 'Save File', filter="Tables (*.csv)", directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        CSVManager.copy_csv(path[0])
        self.ui.model = CSVManager.return_model(False)
        self.ui.tableView.setModel(self.ui.model)
        self.ui.tableView.update()
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {path[0].split('/')[-1]}"))

    # Event method
    def save_clicked(self):
        if SysFilesManager.config["Last_file"] == "None":
            path = QFileDialog.getSaveFileName(self, 'Save File', filter="Tables (*.csv)", directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
            SysFilesManager.config["Last_file"] = path[0]
            CSVManager.save_csv(path[0])
        else:
            CSVManager.save_csv(SysFilesManager.config["Last_file"])
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {SysFilesManager.config['Last_file'].split('/')[-1]}"))

    # Event method
    def save_as_clicked(self):
        path = QFileDialog.getSaveFileName(self, 'Save File', filter="Tables (*.csv)", directory=os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
        SysFilesManager.config["Last_file"] = path[0]
        CSVManager.save_csv(path[0])
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", f"Tasks - {SysFilesManager.config['Last_file'].split('/')[-1]}"))


if __name__ == "__main__":
    SysFilesManager.start()

    app = QApplication([])
    application = Window()
    application.show()

    sys.exit(app.exec())
