  import os
  def get_current_directory():
        return os.getcwd()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]