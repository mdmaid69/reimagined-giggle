import glob
def find_files(pattern):
        return glob.glob(pattern)
def greet(name):
        print(f"Hello, {name}!")