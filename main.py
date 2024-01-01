  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)