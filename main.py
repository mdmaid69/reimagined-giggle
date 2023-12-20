import glob
def find_files(pattern):
        return glob.glob(pattern)
n = 10
print("Square numbers:", [x**2 for x in range(n)])