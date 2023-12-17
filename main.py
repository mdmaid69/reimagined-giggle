  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
print([x**2 for x in range(10)])