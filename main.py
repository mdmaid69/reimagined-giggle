sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)