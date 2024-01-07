  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()