  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()