  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)