import shutil
def delete_directory(path):
        shutil.rmtree(path)
import array
def get_array_as_frozenset(array):
        return frozenset(array)