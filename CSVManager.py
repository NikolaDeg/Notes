import csv
import os
import shutil

from PyQt5.QtGui import QStandardItemModel, QStandardItem

import SysFilesManager
import MessageBoxes


# Copies
def copy_csv(path):
    try:
        SysFilesManager.config["Last_file"] = path
        shutil.copyfile(path, f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}")
    except PermissionError:
        MessageBoxes.error('Something wrong with permissions')
    except Exception as ex:
        MessageBoxes.error(str(ex))


# Returns data to TebleView
def return_model(clear: bool):
    if not clear:
        try:
            model = QStandardItemModel()

            file = open(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}")

            for row in csv.reader(file):
                row = str(row).replace("']", "").replace("['", "").split(";")
                items = [
                    QStandardItem(data)
                    for data in row
                ]
                model.appendRow(items)

            model.setHorizontalHeaderLabels(['Date', 'Time', 'Name', 'Description'])

        except Exception as ex:
            MessageBoxes.error(str(ex))
            return QStandardItemModel().setHorizontalHeaderLabels(['Date', 'Time', 'Name', 'Description'])
        else:
            return model
    else:
        return QStandardItemModel().setHorizontalHeaderLabels(['Date', 'Time', 'Name', 'Description'])


# Creates temporally file
def create_csv():
    path = f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}"
    try:
        file = open(path, "w")
        file.close()
    except FileExistsError:
        MessageBoxes.error('File already exists. Delete it. NOW! Or rename.')


# Copies temporally file
def save_csv(path):
    shutil.copyfile(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}", path)
    SysFilesManager.file_saved = True


# Adds information to temporally file
def add_csv(data):
    try:
        with open(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}", "a+", newline='') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(data)
    except PermissionError:
        MessageBoxes.error("Temporally file opened in other program, close it")
    else:
        SysFilesManager.file_saved = False
