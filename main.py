  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns