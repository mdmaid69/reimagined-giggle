def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))