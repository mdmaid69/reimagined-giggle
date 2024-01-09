import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_base_name(path):
        return os.path.basename(path)