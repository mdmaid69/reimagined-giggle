  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()