  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import array
def check_if_array_contains_item(array, item):
        return item in array