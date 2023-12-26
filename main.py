import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size