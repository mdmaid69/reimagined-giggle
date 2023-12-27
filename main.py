def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))