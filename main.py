import array
def get_bytes_from_array(array):
        return array.tobytes()
import shutil
def delete_directory(path):
        shutil.rmtree(path)