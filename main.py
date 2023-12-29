  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)