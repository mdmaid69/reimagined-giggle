  import os
  def get_current_directory():
        return os.getcwd()
import re
def split_string(pattern, string):
        return re.split(pattern, string)