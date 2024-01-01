import shutil
def delete_directory(path):
        shutil.rmtree(path)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)