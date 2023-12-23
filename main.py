  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)