import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))