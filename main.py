  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)