import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)