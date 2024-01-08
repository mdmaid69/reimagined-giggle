  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import array
def check_if_array_contains_item(array, item):
        return item in array