  import sys
  def get_python_version():
        return sys.version
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()