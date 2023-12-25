  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import re
def split_string(pattern, string):
        return re.split(pattern, string)