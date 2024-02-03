import os


class Path:
    current_file = os.path.abspath('__file__')
    current_directory = os.path.dirname(current_file)
    files_directory = os.path.join(current_directory, 'files')
    resources_directory = os.path.join(current_directory, 'resources')
    archive_directory = os.path.join(resources_directory, 'archive.zip')
    files_list = os.listdir(files_directory)


path_file = Path()
