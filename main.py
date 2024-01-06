  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import re
print(re.match("h.*o", "hello world"))