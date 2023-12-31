import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)