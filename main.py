  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
i = 0
while i < 5:
        print(i)
        i += 1