import shutil
def delete_directory(path):
        shutil.rmtree(path)
import glob
def find_files(pattern):
        return glob.glob(pattern)