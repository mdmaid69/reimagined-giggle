import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)