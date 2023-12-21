import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def split_path(path):
        return os.path.split(path)