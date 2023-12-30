def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))