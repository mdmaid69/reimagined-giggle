  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)