  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()