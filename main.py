import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)