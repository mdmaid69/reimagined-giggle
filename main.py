  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)