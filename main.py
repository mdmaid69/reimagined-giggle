def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))