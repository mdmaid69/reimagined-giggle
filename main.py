import glob
def find_files(pattern):
        return glob.glob(pattern)
text = "Hello, world!"
print("Words:", len(text.split()))