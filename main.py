  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)