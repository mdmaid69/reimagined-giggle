  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import re
def split_string(pattern, string):
        return re.split(pattern, string)