import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)