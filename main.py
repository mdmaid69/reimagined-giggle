  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import array
def check_if_array_contains_item(array, item):
        return item in array