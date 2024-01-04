import os
def remove_directory(path):
        os.rmdir(path)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()