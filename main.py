  def calculate_area_rectangle(l, w):
        return l * w
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()