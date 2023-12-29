import time
def get_time_since_epoch():
        return time.time()
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)