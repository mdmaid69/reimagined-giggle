  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import re
def split_string(pattern, string):
        return re.split(pattern, string)