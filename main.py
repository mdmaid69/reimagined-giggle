import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]