import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode