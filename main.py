  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)