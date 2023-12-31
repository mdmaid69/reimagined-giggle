  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)