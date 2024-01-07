  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)