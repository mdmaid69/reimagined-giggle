  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
i = 0
while i < 5:
        print(i)
        i += 1