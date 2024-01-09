  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array