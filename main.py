  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]