  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)