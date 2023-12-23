  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)