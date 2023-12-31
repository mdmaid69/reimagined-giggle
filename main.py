import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]