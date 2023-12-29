  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
i = 0
while i < 5:
        print(i)
        i += 1