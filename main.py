import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)