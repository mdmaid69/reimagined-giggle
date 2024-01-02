import array
def check_if_array_contains_item(array, item):
        return item in array
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid