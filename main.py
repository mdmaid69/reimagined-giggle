  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import re
def split_string(pattern, string):
        return re.split(pattern, string)