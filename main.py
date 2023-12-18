import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)