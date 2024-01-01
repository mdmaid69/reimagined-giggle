import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)