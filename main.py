print([x**2 for x in range(10)])
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size