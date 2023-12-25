text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import glob
def find_files(pattern):
        return glob.glob(pattern)