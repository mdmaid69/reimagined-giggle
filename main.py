  def remove_duplicates(lst):
        return list(set(lst))
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()