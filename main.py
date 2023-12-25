  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import array
def check_if_array_contains_item(array, item):
        return item in array