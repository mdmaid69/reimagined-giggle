import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns