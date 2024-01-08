import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import os
def get_current_working_directory():
        return os.getcwd()