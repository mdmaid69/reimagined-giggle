  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)