  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]