import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import glob
def find_files(pattern):
        return glob.glob(pattern)