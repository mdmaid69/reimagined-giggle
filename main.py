import os
def list_files_in_directory(path):
        return os.listdir(path)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()