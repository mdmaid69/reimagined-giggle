  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)