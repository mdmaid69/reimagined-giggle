  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import array
def check_if_array_contains_item(array, item):
        return item in array