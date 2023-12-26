  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"