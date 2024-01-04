  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import re
def split_string(pattern, string):
        return re.split(pattern, string)