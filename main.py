  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import re
print(re.match("h.*o", "hello world"))