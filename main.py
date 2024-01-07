  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)