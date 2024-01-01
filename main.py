import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime