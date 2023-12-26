import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  def square_number(x):
        return x**2