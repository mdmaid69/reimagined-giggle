import array
def get_array_as_bytes(array):
        return bytes(array)
import shutil
def delete_directory(path):
        shutil.rmtree(path)