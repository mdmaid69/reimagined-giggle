import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)