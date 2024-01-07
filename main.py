  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)