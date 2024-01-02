import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)