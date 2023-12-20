  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()