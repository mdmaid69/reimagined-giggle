import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a