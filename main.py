import os
def get_current_working_directory():
        return os.getcwd()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()