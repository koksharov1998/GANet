from PIL import Image
import os
import sys
import shutil


files = os.listdir("left")

list_file_name = "dfc_train.list"
with open(list_file_name, "w") as list_file:
    for file_name in files:
        list_file.write("DIPLOM/left/" + file_name + "\n")

