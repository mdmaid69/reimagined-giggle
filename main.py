  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)