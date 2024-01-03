import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a