import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)