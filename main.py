  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)