  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)