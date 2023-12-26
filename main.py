import shutil
def delete_directory(path):
        shutil.rmtree(path)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)