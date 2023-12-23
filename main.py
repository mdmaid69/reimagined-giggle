import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])