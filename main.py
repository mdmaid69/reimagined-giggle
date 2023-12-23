import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def split_path(path):
        return os.path.split(path)