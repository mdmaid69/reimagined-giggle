  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)