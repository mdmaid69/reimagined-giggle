import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def split_path(path):
        return os.path.split(path)