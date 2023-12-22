  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def get_array_item(array, i):
        return array[i]