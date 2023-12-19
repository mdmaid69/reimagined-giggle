import glob
def find_files(pattern):
        return glob.glob(pattern)
n = 10
print("Powers of 2:", [2**x for x in range(n)])