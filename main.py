  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size