import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)