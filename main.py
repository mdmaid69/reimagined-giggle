def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)