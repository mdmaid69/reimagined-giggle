  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
i = 0
while i < 5:
        print(i)
        i += 1