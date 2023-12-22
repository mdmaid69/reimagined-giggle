  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)