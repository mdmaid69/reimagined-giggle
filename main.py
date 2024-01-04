import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)