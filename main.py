  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)