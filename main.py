import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)