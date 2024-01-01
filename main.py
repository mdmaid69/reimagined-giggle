  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)