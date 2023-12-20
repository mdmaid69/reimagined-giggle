  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)