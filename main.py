  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))