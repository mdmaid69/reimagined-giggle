  import os
  def delete_file(file_name):
        os.remove(file_name)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)