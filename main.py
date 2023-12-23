  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)