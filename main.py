  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)