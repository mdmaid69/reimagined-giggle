import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)