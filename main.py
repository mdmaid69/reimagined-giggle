import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time