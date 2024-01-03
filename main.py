import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)