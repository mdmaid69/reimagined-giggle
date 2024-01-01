import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)