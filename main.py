import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import glob
def find_files(pattern):
        return glob.glob(pattern)