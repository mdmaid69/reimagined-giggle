  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()