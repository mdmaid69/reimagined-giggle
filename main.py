  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)