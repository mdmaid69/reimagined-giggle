import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b