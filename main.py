import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks