import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]