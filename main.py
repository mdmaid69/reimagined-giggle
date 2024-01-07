  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import array
def get_array_slice(array, i, j):
        return array[i:j]