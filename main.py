  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)