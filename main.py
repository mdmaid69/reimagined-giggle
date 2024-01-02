  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)