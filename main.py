  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)