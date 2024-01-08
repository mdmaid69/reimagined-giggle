  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"