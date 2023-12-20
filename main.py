  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)