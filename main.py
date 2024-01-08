  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)