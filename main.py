import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)