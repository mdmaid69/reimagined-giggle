import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import random
  def generate_random_number(start, end):
        return random.randint(start, end)