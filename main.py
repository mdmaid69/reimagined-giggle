  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))