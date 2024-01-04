import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns