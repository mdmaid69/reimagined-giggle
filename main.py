import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)