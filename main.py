import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)