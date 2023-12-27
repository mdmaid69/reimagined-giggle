  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)