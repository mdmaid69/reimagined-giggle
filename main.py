  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)