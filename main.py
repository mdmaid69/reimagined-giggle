  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))