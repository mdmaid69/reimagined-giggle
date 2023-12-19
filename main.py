  import os
  def split_path(path):
        return os.path.split(path)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)