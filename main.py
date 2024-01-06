import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)