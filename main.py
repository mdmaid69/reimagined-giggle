import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns