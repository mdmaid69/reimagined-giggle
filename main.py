print([x**2 for x in range(10)])
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns