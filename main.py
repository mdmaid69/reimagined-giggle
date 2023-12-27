  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)