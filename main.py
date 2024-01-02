import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_base_name(path):
        return os.path.basename(path)