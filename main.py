  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
print([x**2 for x in range(10)])