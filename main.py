import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]