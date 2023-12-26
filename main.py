import os
def get_environment_variable(var):
        return os.getenv(var)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()