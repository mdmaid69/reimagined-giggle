import glob
def find_files(pattern):
        return glob.glob(pattern)
i = 0
while i < 5:
        print(i)
        i += 1