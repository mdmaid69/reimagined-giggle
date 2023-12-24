  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import array
def check_if_array_contains_item(array, item):
        return item in array