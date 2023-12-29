  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()