import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino