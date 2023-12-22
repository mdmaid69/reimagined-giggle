  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)