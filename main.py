  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
i = 0
while i < 5:
        print(i)
        i += 1