  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import re
def split_string(pattern, string):
        return re.split(pattern, string)