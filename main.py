import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)