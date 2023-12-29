  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
print([x**2 for x in range(10)])