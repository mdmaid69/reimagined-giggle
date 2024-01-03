import shutil
def move_file(src, dst):
        shutil.move(src, dst)
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))