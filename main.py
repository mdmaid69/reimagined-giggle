  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]