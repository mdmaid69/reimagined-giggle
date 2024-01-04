i = 0
while i < 5:
        print(i)
        i += 1
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino