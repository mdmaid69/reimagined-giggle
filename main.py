  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)