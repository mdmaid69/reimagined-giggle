import shutil
def delete_directory(path):
        shutil.rmtree(path)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()