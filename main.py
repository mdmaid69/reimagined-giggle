  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()