  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)