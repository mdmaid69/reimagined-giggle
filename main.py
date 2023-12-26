import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)