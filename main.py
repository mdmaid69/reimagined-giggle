import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)