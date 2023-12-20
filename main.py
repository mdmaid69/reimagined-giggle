import os
def remove_directory(path):
        os.rmdir(path)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)