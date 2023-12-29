  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]