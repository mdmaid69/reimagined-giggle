  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)