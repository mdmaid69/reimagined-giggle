import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)