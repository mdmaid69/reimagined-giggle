  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import array
def get_array_as_memoryview(array):
        return memoryview(array)