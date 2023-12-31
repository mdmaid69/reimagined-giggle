import array
def get_string_from_array(array):
        return array.tobytes()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)