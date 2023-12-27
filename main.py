  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import array
def get_string_from_array(array):
        return array.tobytes()