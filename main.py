  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import re
def split_string(pattern, string):
        return re.split(pattern, string)