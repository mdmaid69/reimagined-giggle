  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)