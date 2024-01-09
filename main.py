import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import os
def change_working_directory(path):
        os.chdir(path)