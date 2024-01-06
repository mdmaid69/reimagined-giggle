  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]