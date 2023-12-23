import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)