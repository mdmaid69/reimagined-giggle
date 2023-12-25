  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import array
def set_array_item(array, i, item):
        array[i] = item