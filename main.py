  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)