  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
print([x**2 for x in range(10)])