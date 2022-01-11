import csv
import os
import shutil

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QErrorMessage

import SysFilesManager


def copyCSV(path):
    try:
        SysFilesManager.config["Last_file"] = path
        shutil.copyfile(path, f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}")
    except Exception:
        SysFilesManager.repair()


def returnModel(clear: bool):
    if clear:
        return QStandardItemModel()
    else:
        try:
            model = QStandardItemModel()
            with open(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}",
                      "r") as file:
                for row in csv.reader(file):
                    row = str(row).replace("']", "").replace("['", "").split(";")
                    items = [
                        QStandardItem(data)
                        for data in row
                    ]
                    model.appendRow(items)

            return model
        except Exception:
            SysFilesManager.repair()


def createCSV():
    try:
        SysFilesManager.config["Last_file"] = "None"
        for filename in os.listdir(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}"):
            file_path = os.path.join(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}", filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                error_dialog = QErrorMessage()
                error_dialog.showMessage(f'Failed to delete {file_path}. Reason: {e}')

        fullPath = f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}"
        file = None
        try:
            file = open(fullPath, "x")
        except FileExistsError:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('File already exists. Delete it. NOW! Or rename.')
        finally:
            if file is not None:
                file.close()
    except Exception:
        SysFilesManager.repair()


def saveCSV(path):
    shutil.copyfile(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}", path)
    SysFilesManager.file_saved = True


def addCSV(data):
    with open(f"{SysFilesManager.system_dir_name}/{SysFilesManager.temp_dir_name}/{SysFilesManager.temp_name}", "a+", newline='') as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(data)
    SysFilesManager.file_saved = False
