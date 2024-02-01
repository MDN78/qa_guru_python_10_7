import os
import shutil
import pytest
from utils.path import Path as P
from utils.script_zip_unzip import add_files_to_zip, extract_files

@pytest.fixture
def directory_manager():
    if not os.path.exists(P.resources_directory):
        os.mkdir(P.resources_directory)
        add_files_to_zip()
        extract_files()

    yield
    shutil.rmtree(P.resources_directory)

