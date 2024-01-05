  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import re
print(re.match("h.*o", "hello world"))