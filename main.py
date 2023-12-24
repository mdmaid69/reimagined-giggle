  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)