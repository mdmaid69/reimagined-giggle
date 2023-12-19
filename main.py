  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)