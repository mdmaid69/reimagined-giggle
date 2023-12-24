text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)