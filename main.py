import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import glob
def find_files(pattern):
        return glob.glob(pattern)