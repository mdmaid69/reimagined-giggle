  import os
  def get_base_name(path):
        return os.path.basename(path)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)