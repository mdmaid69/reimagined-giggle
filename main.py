import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)