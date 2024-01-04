import glob
def find_files(pattern):
        return glob.glob(pattern)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()