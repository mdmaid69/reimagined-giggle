import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)