  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
print([x**2 for x in range(10)])