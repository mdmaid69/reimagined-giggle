import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)