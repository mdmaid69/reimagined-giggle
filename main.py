  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}