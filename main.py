  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)