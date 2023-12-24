  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import re
def split_string(pattern, string):
        return re.split(pattern, string)