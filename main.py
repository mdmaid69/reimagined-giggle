  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)