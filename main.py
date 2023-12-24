  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)