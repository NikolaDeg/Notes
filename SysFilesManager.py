import os
import shutil
import main

config = {}

system_dir_name = "system"  #
config_name = "sys.con" # f"{system_dir_name}/{config_dir_name}/{config_name}"
temp_dir_name = "temp"  # f"{system_dir_name}/{temp_dir_name}"
config_dir_name = "config"  # f"{system_dir_name}/{config_dir_name}"
config_splitter = "->"
temp_name = "temp.csv"

file_saved = True


def initialization():
    config["Last_file"] = "None"
    config["Trick"] = "None"

    file = None
    try:
        os.mkdir(system_dir_name)
        os.mkdir(f"{system_dir_name}/{temp_dir_name}")
        os.mkdir(f"{system_dir_name}/{config_dir_name}")

        file = open(f"{system_dir_name}/{config_dir_name}/{config_name}", "w")

        for i in config.keys():
            file.write(f"{i}{config_splitter}{config[i]}\n")

        file.close()
    except Exception:
        repair()


def repair():
    try:
        shutil.rmtree(system_dir_name)
    except Exception:
        pass
    initialization()


def new_repair(path):
    try:
        open(path, "w")
    except Exception as ex:
        main.Window.error(str(ex))


#def new_initializaion()

def check():
    path = f"{system_dir_name}/{config_dir_name}/{config_name}"
    try:
        file = open(path, "r")
        for row in file.readlines():
            row = row.replace("\n", "").split(config_splitter)
            config[row[0]] = row[1]
            file.close()
    except FileNotFoundError:
        new_repair(path)
    except PermissionError:
        main.Window.error("Файл конфигурации открыт в другой программе, закроёте её.")
    except Exception:
        repair()
        