import os
print(os.getcwd())
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()