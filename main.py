import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)