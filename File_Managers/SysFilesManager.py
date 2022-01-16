import os
from Auxiliary import MessageBoxes

config = {}

config["Last_file"] = "None"
config["Trick"] = "None"

system_dir_name = "../system"  #
config_name = "sys.con" # f"{system_dir_name}/{config_dir_name}/{config_name}"
temp_dir_name = "temp"  # f"{system_dir_name}/{temp_dir_name}"
config_dir_name = "config"  # f"{system_dir_name}/{config_dir_name}"
config_splitter = " -> "
temp_name = "temp.csv"

file_saved = True

system_directories = [system_dir_name, f"{system_dir_name}/{temp_dir_name}", f"{system_dir_name}/{config_dir_name}"]
system_files = [f"{system_dir_name}/{config_dir_name}/{config_name}"]


# Writs config file and catching exceptions
def write_config_file():
    path = f"{system_dir_name}/{config_dir_name}/{config_name}"

    # Trying to write data
    try:
        file = open(path, "w")

        for i in config.keys():
            file.write(f"{i}{config_splitter}{config[i]}\n")

        file.close()
    except FileNotFoundError:
        create_file(path)
    except Exception as ex:
        MessageBoxes.error(str(ex))


# Reads config file and catching exceptions
def read_config_file():
    path = f"{system_dir_name}/{config_dir_name}/{config_name}"

    # Trying to read data
    try:
        file = open(path, "r")

        for row in file.readlines():
            row = row.replace("\n", "").split(config_splitter)

            try:
                config[row[0]] = row[1]
            except KeyError:
                write_config_file()
            except Exception as ex:
                MessageBoxes.error(str(ex))

        file.close()
    except FileNotFoundError:
        create_file(path)
        read_config_file()
    except PermissionError:
        main.Window.error("File opened in other program, close it")
    except Exception as ex:
        MessageBoxes.error(str(ex))


# Creates directories and catching exceptions
def create_directory(dir):
    try:
        os.mkdir(dir)
    except Exception as ex:
        MessageBoxes.error(str(ex))


# Creates file and catching exceptions
def create_file(dir):
    try:
        file = open(dir, "w")
        file.close()
    except Exception as ex:
        MessageBoxes.error(str(ex))


# Checks system files and directories, reading confing
def start():
    for path in system_directories:
        if not os.path.exists(path):
            create_directory(path)

    for path in system_files:
        if not os.path.exists(path):
            create_file(path)

    read_config_file()
