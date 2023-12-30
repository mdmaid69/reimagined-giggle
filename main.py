  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)