  import os
  def get_base_name(path):
        return os.path.basename(path)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)