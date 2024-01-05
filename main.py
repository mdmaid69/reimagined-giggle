import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)