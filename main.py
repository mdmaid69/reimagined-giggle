import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def delete_file(file_name):
        os.remove(file_name)