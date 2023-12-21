import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)