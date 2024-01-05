import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2