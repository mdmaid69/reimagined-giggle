import shutil
def move_file(src, dst):
        shutil.move(src, dst)
text = "Hello, world!"
print("Words:", len(text.split()))