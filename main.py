  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)