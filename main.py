  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()