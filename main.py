import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size