  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()