import os
import shutil
import pytest
from utils.path import path_file
from utils.script_zip_unzip import add_files_to_zip, extract_files

@pytest.fixture(scope='function', autouse=True)
def directory_manager():
    if not os.path.exists(path_file.resources_directory):
        os.mkdir(path_file.resources_directory)
        add_files_to_zip()
        extract_files()

    yield
    shutil.rmtree(path_file.resources_directory)

