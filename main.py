  import os
  def get_current_directory():
        return os.getcwd()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)