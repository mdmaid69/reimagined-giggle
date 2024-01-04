  import os
  def get_current_directory():
        return os.getcwd()
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)