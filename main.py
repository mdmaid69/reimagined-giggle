import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import glob
def find_files(pattern):
        return glob.glob(pattern)