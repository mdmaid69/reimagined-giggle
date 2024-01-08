  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def split_path(path):
        return os.path.split(path)