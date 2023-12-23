  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
for i in range(5):
        print(i)