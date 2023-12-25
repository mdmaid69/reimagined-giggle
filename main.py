  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]