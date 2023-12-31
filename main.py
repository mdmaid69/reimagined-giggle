  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)