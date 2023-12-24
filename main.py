  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array