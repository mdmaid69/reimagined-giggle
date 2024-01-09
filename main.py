import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime