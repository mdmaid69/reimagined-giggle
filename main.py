  import os
  def delete_file(file_name):
        os.remove(file_name)
import array
def get_array_as_memoryview(array):
        return memoryview(array)