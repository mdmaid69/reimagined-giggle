  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import re
print(re.match("h.*o", "hello world"))