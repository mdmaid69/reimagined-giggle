import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import shutil
def delete_directory(path):
        shutil.rmtree(path)