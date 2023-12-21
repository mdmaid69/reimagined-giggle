import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)