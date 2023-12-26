import array
def set_array_item(array, i, item):
        array[i] = item
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen