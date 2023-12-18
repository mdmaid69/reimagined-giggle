import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size