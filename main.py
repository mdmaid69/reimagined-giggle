import time
def get_time_since_epoch():
        return time.time()
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)