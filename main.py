  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)