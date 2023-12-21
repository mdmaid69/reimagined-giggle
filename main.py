  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import re
print(re.match("h.*o", "hello world"))