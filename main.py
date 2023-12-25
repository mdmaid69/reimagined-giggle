  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array