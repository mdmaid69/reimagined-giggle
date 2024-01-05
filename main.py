  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)