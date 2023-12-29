  import os
  def split_path(path):
        return os.path.split(path)
import array
def get_array_as_memoryview(array):
        return memoryview(array)