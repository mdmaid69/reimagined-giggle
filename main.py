import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import glob
def find_files(pattern):
        return glob.glob(pattern)