import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)