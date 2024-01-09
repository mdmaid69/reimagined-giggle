import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev