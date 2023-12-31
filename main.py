import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import glob
def find_files(pattern):
        return glob.glob(pattern)