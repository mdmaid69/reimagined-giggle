  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)