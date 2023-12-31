  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)