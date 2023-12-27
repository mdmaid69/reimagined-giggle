import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)