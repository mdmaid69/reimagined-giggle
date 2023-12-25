import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)