import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities