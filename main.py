import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import os
def change_working_directory(path):
        os.chdir(path)