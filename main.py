  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]