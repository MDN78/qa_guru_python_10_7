from zipfile import ZipFile
from utils.path import path_file
import os


def add_files_to_zip():
    with ZipFile(path_file.archive_directory, mode='w') as myzip:
        for file in path_file.files_list:
            add = os.path.join(path_file.files_directory, file)
            myzip.write(add, os.path.basename(add))


def extract_files():
    with ZipFile(path_file.archive_directory, mode='r') as unzip:
        unzip.extractall(path_file.resources_directory)
