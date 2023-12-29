  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks