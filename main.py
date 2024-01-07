  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)