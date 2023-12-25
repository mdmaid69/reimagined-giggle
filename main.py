  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)