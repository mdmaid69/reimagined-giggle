import re
print(re.match("h.*o", "hello world"))
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime