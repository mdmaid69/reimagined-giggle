  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def check_if_array_contains_item(array, item):
        return item in array