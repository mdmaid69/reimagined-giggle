  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()