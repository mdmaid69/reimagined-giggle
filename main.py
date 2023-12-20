  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
i = 0
while i < 5:
        print(i)
        i += 1