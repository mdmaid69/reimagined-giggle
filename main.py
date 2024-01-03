  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)