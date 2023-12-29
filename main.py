  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import os
def change_working_directory(path):
        os.chdir(path)