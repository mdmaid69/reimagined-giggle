  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)