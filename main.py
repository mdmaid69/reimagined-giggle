  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)