import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import shutil
def delete_directory(path):
        shutil.rmtree(path)