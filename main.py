  import os
  def get_current_working_directory():
        return os.getcwd()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)