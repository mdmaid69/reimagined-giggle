def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)