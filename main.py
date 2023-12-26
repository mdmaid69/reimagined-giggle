import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def delete_file(file_name):
        os.remove(file_name)