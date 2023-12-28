import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)