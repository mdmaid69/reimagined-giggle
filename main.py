text = "Hello, world!"
print("Words:", len(text.split()))
import shutil
def move_file(src, dst):
        shutil.move(src, dst)