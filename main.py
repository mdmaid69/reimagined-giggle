  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b