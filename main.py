import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)