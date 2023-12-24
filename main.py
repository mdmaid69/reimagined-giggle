import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)