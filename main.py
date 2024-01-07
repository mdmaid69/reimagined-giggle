import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import os
def list_files_in_directory(path):
        return os.listdir(path)