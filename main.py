for i in range(5):
        print(i)
  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev