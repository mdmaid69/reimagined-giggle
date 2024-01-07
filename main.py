import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)