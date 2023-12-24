  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])