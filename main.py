  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()