  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)