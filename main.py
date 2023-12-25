import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)