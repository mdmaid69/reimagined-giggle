  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)