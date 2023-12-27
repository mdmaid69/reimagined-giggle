  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import os
def remove_directory(path):
        os.rmdir(path)