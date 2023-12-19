import os
def list_files_in_directory(path):
        return os.listdir(path)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]