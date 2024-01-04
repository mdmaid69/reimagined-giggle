import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen