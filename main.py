  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)