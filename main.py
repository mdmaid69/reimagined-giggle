import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)