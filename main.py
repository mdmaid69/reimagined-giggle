  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)