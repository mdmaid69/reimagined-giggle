  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)