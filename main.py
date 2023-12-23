import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)