import os
def change_working_directory(path):
        os.chdir(path)
text = "Hello, world!"
print("Words:", len(text.split()))