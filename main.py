  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import array
def check_if_array_contains_item(array, item):
        return item in array