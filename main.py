  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
i = 0
while i < 5:
        print(i)
        i += 1