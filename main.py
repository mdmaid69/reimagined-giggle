  import os
  def get_base_name(path):
        return os.path.basename(path)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)