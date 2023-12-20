import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import os
  def delete_file(file_name):
        os.remove(file_name)