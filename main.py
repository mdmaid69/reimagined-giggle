import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)