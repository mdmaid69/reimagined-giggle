import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import shutil
def delete_directory(path):
        shutil.rmtree(path)