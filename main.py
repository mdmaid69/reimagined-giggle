  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)