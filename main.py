import shutil
def move_file(src, dst):
        shutil.move(src, dst)
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])