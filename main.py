  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
i = 0
while i < 5:
        print(i)
        i += 1