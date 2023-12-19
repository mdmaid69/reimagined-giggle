  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)