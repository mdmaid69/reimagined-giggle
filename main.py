  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)