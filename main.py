  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)