import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)