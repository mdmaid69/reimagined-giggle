import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)