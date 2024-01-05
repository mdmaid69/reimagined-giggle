  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()