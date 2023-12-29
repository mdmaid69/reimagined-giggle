  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]