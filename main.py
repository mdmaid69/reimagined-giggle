  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)