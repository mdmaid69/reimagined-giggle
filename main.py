import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"