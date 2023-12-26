  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import os
def get_file_size(filename):
        return os.path.getsize(filename)