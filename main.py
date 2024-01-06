import array
def convert_array_to_bytes(array):
        return array.tobytes()
import shutil
def delete_directory(path):
        shutil.rmtree(path)