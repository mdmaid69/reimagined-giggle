import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import shutil
def delete_directory(path):
        shutil.rmtree(path)