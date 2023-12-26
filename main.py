  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]