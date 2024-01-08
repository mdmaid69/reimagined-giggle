def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))