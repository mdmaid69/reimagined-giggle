  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)