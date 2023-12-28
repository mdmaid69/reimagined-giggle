  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]