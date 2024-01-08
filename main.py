import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)