  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
i = 0
while i < 5:
        print(i)
        i += 1