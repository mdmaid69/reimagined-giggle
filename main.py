import glob
def find_files(pattern):
        return glob.glob(pattern)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])