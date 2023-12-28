  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"