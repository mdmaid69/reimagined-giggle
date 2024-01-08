  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import re
def split_string(pattern, string):
        return re.split(pattern, string)