  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)