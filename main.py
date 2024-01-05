import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)