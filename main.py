  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)