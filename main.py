  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)