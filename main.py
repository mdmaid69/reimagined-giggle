import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)