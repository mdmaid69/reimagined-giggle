  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)