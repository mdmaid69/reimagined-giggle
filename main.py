  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import array
def check_if_array_contains_item(array, item):
        return item in array