  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import re
def split_string(pattern, string):
        return re.split(pattern, string)