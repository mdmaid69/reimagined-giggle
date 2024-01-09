  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)