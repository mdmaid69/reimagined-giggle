  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]