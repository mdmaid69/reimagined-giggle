  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)