  import os
  def split_path(path):
        return os.path.split(path)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)