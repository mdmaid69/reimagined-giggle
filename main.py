  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)