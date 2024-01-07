import glob
def find_files(pattern):
        return glob.glob(pattern)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)