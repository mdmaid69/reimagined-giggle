  import os
  def get_base_name(path):
        return os.path.basename(path)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)