import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)