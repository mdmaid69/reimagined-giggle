  import os
  def get_base_name(path):
        return os.path.basename(path)
import array
def get_array_as_memoryview(array):
        return memoryview(array)