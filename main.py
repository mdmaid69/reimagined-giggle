  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)