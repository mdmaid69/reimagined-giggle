  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
for i in range(10): print(i)