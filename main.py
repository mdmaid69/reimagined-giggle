import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)