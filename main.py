  import os
  def get_current_working_directory():
        return os.getcwd()
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)