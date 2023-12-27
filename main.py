import glob
def find_files(pattern):
        return glob.glob(pattern)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])