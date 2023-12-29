import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)