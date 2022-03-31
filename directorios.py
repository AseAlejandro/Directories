import os
import fleep
from pathlib import Path
import csv

path = "C://Users//Alejandro//Desktop//Trabajo//Python//Directorios//Pictures"

for subdir, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(subdir, file))
