  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)