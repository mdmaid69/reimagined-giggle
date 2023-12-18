import shutil
def delete_directory(path):
        shutil.rmtree(path)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)