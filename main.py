import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)