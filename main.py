  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)