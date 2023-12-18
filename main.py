import glob
def find_files(pattern):
        return glob.glob(pattern)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])