  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import re
def split_string(pattern, string):
        return re.split(pattern, string)