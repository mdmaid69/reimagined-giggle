  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))