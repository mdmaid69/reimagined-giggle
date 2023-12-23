  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import re
def split_string(pattern, string):
        return re.split(pattern, string)