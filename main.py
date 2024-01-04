import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))