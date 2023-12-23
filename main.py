import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]