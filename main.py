  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
i = 0
while i < 5:
        print(i)
        i += 1