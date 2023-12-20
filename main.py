  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import re
def split_string(pattern, string):
        return re.split(pattern, string)