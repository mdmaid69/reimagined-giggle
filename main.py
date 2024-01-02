  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array