  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import re
print(re.match("h.*o", "hello world"))