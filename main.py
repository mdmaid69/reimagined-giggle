import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)