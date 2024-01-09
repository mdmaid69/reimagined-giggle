  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)