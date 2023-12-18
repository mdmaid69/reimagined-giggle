import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)