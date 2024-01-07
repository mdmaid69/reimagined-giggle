import os
def remove_directory(path):
        os.rmdir(path)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)