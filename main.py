  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)