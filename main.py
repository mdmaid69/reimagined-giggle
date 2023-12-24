import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def delete_file(file_name):
        os.remove(file_name)