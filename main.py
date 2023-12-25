  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import re
def split_string(pattern, string):
        return re.split(pattern, string)