import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare