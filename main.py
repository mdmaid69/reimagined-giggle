  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import re
def split_string(pattern, string):
        return re.split(pattern, string)