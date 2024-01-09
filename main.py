import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)