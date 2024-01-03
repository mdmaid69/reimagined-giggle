import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  def calculate_area_triangle(b, h):
        return 0.5 * b * h