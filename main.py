  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])