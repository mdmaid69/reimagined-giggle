import glob
def find_files(pattern):
        return glob.glob(pattern)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])