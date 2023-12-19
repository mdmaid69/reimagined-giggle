  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)