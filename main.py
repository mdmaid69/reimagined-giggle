  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)