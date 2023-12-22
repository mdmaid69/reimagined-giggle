import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def get_base_name(path):
        return os.path.basename(path)