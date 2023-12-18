import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)