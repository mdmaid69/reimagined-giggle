import array
def convert_array_to_bytes(array):
        return array.tobytes()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)