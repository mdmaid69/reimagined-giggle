  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()