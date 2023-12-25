  import os
  def get_current_working_directory():
        return os.getcwd()
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns