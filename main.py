  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import array
def check_if_array_contains_item(array, item):
        return item in array