from zipfile import ZipFile
from utils.path import Path as P
import os

def add_files_to_zip():
    with ZipFile(P.archive_directory, mode='w') as myzip:
        for file in P.files_list:
            add = os.path.join(P.files_directory, file)
            myzip.write(add, os.path.basename(add))

def extract_files():
    with ZipFile(P.archive_directory, mode='r') as unzip:
        unzip.extractall(P.resources_directory)
