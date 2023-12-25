import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
text = "Hello, world!"
print("Words:", len(text.split()))