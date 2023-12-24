import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)