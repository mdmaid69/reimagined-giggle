import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import shutil
def delete_directory(path):
        shutil.rmtree(path)