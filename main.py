import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)