import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode