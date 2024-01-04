  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))