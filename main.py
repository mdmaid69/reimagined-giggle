import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"