  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)