import os
def get_file_size(filename):
        return os.path.getsize(filename)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()