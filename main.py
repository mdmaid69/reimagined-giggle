  import os
  def split_path(path):
        return os.path.split(path)
import re
def split_string(pattern, string):
        return re.split(pattern, string)