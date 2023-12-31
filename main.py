  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
i = 0
while i < 5:
        print(i)
        i += 1