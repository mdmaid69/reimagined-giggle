import glob
def find_files(pattern):
        return glob.glob(pattern)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])