import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)