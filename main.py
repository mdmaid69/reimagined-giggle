  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)