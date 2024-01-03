  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)