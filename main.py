  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()