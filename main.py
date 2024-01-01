  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import re
def split_string(pattern, string):
        return re.split(pattern, string)