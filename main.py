import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)