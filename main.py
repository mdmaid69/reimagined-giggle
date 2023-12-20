import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns