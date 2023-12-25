  import os
  def get_current_working_directory():
        return os.getcwd()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]