  import os
  def get_current_directory():
        return os.getcwd()
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)