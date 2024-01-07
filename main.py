import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import os
def remove_directory(path):
        os.rmdir(path)