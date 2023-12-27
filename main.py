import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)