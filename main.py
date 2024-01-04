  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()