import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)