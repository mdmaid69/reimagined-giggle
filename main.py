  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import array
def convert_array_to_string(array):
        return array.tostring()