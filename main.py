import shutil
def delete_directory(path):
        shutil.rmtree(path)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)