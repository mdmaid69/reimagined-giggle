  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)