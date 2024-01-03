  import os
  def get_current_directory():
        return os.getcwd()
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen