import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)