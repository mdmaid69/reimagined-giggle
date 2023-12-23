  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)