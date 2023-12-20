def calculate_roi(gain, cost):
        return (gain - cost) / cost
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))