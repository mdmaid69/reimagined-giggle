  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]