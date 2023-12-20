  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import re
print(re.match("h.*o", "hello world"))