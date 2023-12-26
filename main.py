import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import glob
def find_files(pattern):
        return glob.glob(pattern)