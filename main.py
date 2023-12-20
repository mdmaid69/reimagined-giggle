  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)