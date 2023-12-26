import glob
def find_files(pattern):
        return glob.glob(pattern)
text = "Hello, world!"
print("Reversed:", text[::-1])