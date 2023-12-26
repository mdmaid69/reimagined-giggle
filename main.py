  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import os
def change_working_directory(path):
        os.chdir(path)