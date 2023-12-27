  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))