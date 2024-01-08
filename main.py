  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)