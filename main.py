  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array