  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)