import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"