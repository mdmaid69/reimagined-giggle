text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
import shutil
def delete_directory(path):
        shutil.rmtree(path)