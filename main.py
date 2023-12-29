import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)