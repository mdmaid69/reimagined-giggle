  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)