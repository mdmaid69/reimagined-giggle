import sklearn.datasets
print(sklearn.datasets.load_iris())
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))