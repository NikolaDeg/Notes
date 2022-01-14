import os
import shutil

config = {}

system_dir_name = "system"  #
config_name = "sys.con"  # f"{system_dir_name}/{config_dir_name}/{config_name}"
temp_dir_name = "temp"  # f"{system_dir_name}/{temp_dir_name}"
config_dir_name = "config"  # f"{system_dir_name}/{config_dir_name}"
config_splitter = " -> "
temp_name = "temp.csv"

file_saved = True


def initialization():
    config["Last_file"] = "None"
    config["Trick"] = "None"

    try:
        os.mkdir(system_dir_name)
        os.mkdir(f"{system_dir_name}/{temp_dir_name}")
        os.mkdir(f"{system_dir_name}/{config_dir_name}")

        file = open(f"{system_dir_name}/{config_dir_name}/{config_name}", "w")

        for i in config.keys():
            file.write(f"{i}{config_splitter}{config[i]}\n")

        file.close()
    except:
        repair()


def check():
    try:
        try:
            file = open(f"{system_dir_name}/{config_dir_name}/{config_name}", "r")
            for row in file.readlines():
                row = row.replace("\n", "").split(config_splitter)
                try:
                    config[row[0]] = row[1]
                except KeyError:
                    repair()
            file.close()
        except:
            initialization()
    except:
        repair()


def repair():
    try:
        shutil.rmtree(system_dir_name)
    except:
        pass
    initialization()
