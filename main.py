  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
for i in range(5):
        print(i)