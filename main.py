  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()