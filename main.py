import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)