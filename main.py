  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import re
def split_string(pattern, string):
        return re.split(pattern, string)