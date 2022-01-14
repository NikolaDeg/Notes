import os
import shutil

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
    except Exception:
        if file is not None:
            file.close()
        repair()
    finally:
        if file is not None:
            file.close()


def repair():
    try:
        shutil.rmtree(system_dir_name)
    except Exception:
        pass
    initialization()


def check():
    try:
        if "sys.con" in os.listdir(f"{system_dir_name}/{config_dir_name}"):

            file = None
            try:
                file = open(f"{system_dir_name}/{config_dir_name}/{config_name}", "r")
                for row in file.readlines():
                    row = row.split(config_splitter)
                    config[row[0]] = config[row[1]]
            except FileNotFoundError:
                file.close()
                initialization()
            finally:
                if file is not None:
                    file.close()
        else:
            initialization()
    except Exception:
        repair()
        