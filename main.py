import os
def change_working_directory(path):
        os.chdir(path)
text = "Hello, world!"
print("Reversed:", text[::-1])