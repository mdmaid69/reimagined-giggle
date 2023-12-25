import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import shutil
def delete_directory(path):
        shutil.rmtree(path)