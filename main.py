import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()